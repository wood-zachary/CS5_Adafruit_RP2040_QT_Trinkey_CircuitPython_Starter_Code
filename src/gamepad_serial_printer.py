import time
from .abstract import MiniGamepad
from support.mytyping import NoReturn

LOOP_DELAY = 0.2

def run_gamepad_serial_printer(gamepad: MiniGamepad) -> NoReturn:
    while True:
        x = gamepad.x
        y = gamepad.y

        a = gamepad.button_a
        b = gamepad.button_b
        x_btn = gamepad.button_x
        y_btn = gamepad.button_y
        start = gamepad.button_start
        select = gamepad.button_select

        print(f"Joystic: X - {x} \tY - {y}")

        buttons = "Buttons:"
        if a:
            buttons += " A"
        if b:
            buttons += " B"
        if x_btn:
            buttons += " X"
        if y_btn:
            buttons += " Y"
        if start:
            buttons += " Start"
        if select:
            buttons += " Select"
        if buttons == "Buttons:":
            buttons += " (none)"

        print(buttons)
        print()

        time.sleep(LOOP_DELAY)
