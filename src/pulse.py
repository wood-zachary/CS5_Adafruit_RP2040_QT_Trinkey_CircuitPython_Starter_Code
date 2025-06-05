import time

from .abstract import LEDController
from support.mytyping import NoReturn

THRESHOLD: int = 75
BLUE: tuple[int, int, int] = (0, 0, 255)
TIME: int = 1


def pulse(px: LEDController, color: tuple[int, int, int], duration: float) -> None:
    """
    Fills pixels with a color for a duration, then turns them off.

    Args:
        px (): LED controller object.
        color (tuple): Color to display.
        duration (float): time in seconds to keep the color on/off.
    """
    px.fill(color)
    time.sleep(duration)
    px.fill((0,0,0))
    time.sleep(duration)


def run_simple_pulse(pixels: LEDController) -> NoReturn:
    """
    Runs a simple pulse demo.

    Args:
        pixels: LED controller object.
    """
    # Main loop
    while True:
        pulse(pixels, BLUE, TIME)
