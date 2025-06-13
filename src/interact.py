from .gamepad_serial_printer import run_gamepad_serial_printer
from .nunchuk_serial_printer import run_nunchuk_serial_printer
from .pulse import run_simple_pulse
from .nunchuk_space_macro import run_nunchuk_space_macro
from .gamepad_space_macro import run_gamepad_space_macro

def run(
    *,
    apds=None,
    pixels=None,
    touch1=None,
    touch2=None, 
    nunchuk=None,
    gamepad=None
):
    """
    Runs the selected demo on the Trinkey.

    Args:
        proximity   — APDS9960 proximity sensor
        pixels      — LEDController
        touch1      — TouchSensor
        touch2      — TouchSensor
        nunchuk     — Nunchuk controller
        gamepad     — MiniGamepad controller
    """
    run_gamepad_serial_printer(gamepad)
    # run_nunchuk_serial_printer(nunchuk)
    # run_simple_pulse(pixels)
    # run_nunchuk_space_macro(nunchuk, pixels)
    # run_gamepad_space_macro(gamepad, pixels)