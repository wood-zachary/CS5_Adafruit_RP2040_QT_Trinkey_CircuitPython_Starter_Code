import subprocess
import time
import platform
import shutil
import os
import ports
import urllib.request
import ssl
from pathlib import Path
import sys

try:
    import psutil
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'psutil'])
finally:
    import psutil

ssl._create_default_https_context = ssl._create_unverified_context


def get_drive():

    def get_windows_drive_name(letter):
        return subprocess.check_output(["cmd", "/c vol " + letter]).decode().split("\r\n")[0].split(" ").pop()

    if platform.system().lower() == 'windows':
        disks = [(x.mountpoint, get_windows_drive_name(x.mountpoint.strip('\\')))
                 for x in psutil.disk_partitions()]
        disks = [(x, name)
                 for x, name in disks if 'TRINKEY' in name or 'CIRCUIT' in name]
    else:
        disks = [(x.mountpoint, x.mountpoint) for x in psutil.disk_partitions(
        ) if 'TRINKEY' in x.mountpoint.upper() or 'CIRCUIT' in x.mountpoint.upper()]

    if len(disks) != 1:
        print("Could not find the Trinkey.  Did you click the reset button twice and connect it?")
        exit(1)

    disk, name = disks[0]
    return disk, name


def reset_drive():
    urllib.request.urlretrieve(
        "https://downloads.circuitpython.org/bin/adafruit_proxlight_trinkey_m0/en_US/adafruit-circuitpython-adafruit_proxlight_trinkey_m0-en_US-9.1.4.uf2", os.path.join(
            disk, 'trinkey.uf2'))
    print("The drive will now eject and then re-attach.  Please wait 10 seconds.")
    time.sleep(10)


disk, name = get_drive()
if 'TRINKEY' in name:
    reset_drive()

disk, name = get_drive()
trinkey = ports.get_trinkey_port()
if not trinkey:
    print("Could not find the Trinkey to connect to...try removing it from the USB drive and plugging it back in.")
    exit(1)

print("Connected to Trinkey! Transfering files...")

shutil.rmtree(os.path.join('src', '__pycache__'), True)
shutil.rmtree(os.path.join('support', '__pycache__'), True)
shutil.rmtree(os.path.join('src', '.mypy_cache'), True)
shutil.rmtree(os.path.join('support', '.mypy_cache'), True)


shutil.rmtree(disk, True)

shutil.copytree('src', os.path.join(disk, 'src'), dirs_exist_ok=True)
shutil.copytree('support', os.path.join(disk, 'support'), dirs_exist_ok=True)
shutil.copytree('lib', os.path.join(disk, 'lib'), dirs_exist_ok=True) 
shutil.copytree('setup', os.path.join(disk, 'setup'), dirs_exist_ok=True) 

# Kill any running program
trinkey.write(bytes(chr(0x03), 'utf-8'))
trinkey.flush()

Path(os.path.join(disk, 'code.py')).write_bytes(Path("code.py").read_bytes())

print("Files transfered...connecting to Trinkey...")
trinkey.flush()
time.sleep(5)

print("Restarting Trinkey!")
trinkey.write(bytes(chr(0x04), 'utf-8'))
trinkey.flush()

miniterm = ports.connect_to_serial(trinkey)
