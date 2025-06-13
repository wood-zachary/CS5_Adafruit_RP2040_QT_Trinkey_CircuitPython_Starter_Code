import time
from adafruit_nunchuk import Nunchuk
from support.mytyping import NoReturn

LOOP_DELAY = 0.2

def run_nunchuk_serial_printer(nunchuk: Nunchuk) -> NoReturn:
    while True:
        ax, ay, az = nunchuk.acceleration
        jx, jy = nunchuk.joystick
        c_pressed = nunchuk.buttons.C
        z_pressed = nunchuk.buttons.Z

        print(f"Acceleration: X - {ax} \tY - {ay} \tZ - {az}")
        print(f"Joystic: X - {jx} \tY - {jy}")

        buttons = "Buttons:"
        if c_pressed:
            buttons += " C"
        if z_pressed:
            buttons += " Z"
        if buttons == "Buttons:":
            buttons += " (none)"

        print(buttons)
        print()

        time.sleep(LOOP_DELAY)
