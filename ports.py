import subprocess
import sys

try:
    import serial
    import serial.tools
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'pyserial'])
finally:
    import serial
    import serial.tools

import serial.tools.list_ports
import serial.tools.miniterm

CTRL_C = bytes(0x03)
CTRL_D = bytes(0x04)
CTRL_C_SUB = bytes(0x7F)


def get_trinkey_port():
    ports = serial.tools.list_ports.comports()
    for port, desc, hwid in sorted(ports):
        if 'Trinkey' in desc or '239A' in desc.upper() or '239A' in hwid.upper():
            s = serial.Serial(port, baudrate=115200)
            return s
    return None


def connect_to_serial(s):
    class NoCTRLC(serial.tools.miniterm.Transform):
        def tx(self, text):
            return text.replace('k', chr(0x03)).replace('r', chr(0x4))

    serial.tools.miniterm.TRANSFORMATIONS['ctrlc'] = NoCTRLC
    miniterm = serial.tools.miniterm.Miniterm(
        s, echo=False, filters=('ctrlc',))
    miniterm.exit_character = chr(0x03)
    miniterm.menu_character = chr(0x0D)
    miniterm.raw = True
    miniterm.set_rx_encoding('UTF-8')
    miniterm.set_tx_encoding('UTF-8')
    sys.stderr.write('--- Miniterm on {p.name}  {p.baudrate},{p.bytesize},{p.parity},{p.stopbits} ---\n'.format(
        p=miniterm.serial))
    sys.stderr.write('--- Quit: {} ---\n'.format(
        serial.tools.miniterm.key_description(miniterm.exit_character)))
    miniterm.start()

    miniterm.join()
    sys.stderr.write('\n--- exit ---\n')
    miniterm.close()
