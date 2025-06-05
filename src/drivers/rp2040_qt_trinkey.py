# src/drivers/rp2040_qt_trinkey.py

import board
import neopixel
from src.abstract import LEDController

class _TrinkeyLEDs(LEDController):
    """Driver for the single NeoPixel on the RP2040 QT Trinkey."""

    def __init__(self, brightness: float = 0.1):
        self._pixel = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=brightness)

    def fill(self, color: tuple[int, int, int]) -> None:
        """Set the NeoPixel to a given RGB color."""
        self._pixel.fill(color)


def make_rp2040_qt_trinkey_devices() -> LEDController:
    """
    Returns an instance of _TrinkeyLEDs (implements LEDController).

    Usage (in code.py):
        from src.drivers.rp2040_qt_trinkey import make_rp2040_qt_trinkey_led
        from src.interact import run

        i2c = board.I2C()
        leds = make_rp2040_qt_trinkey_led()
        run(leds)           # or run(<your_device>, leds) if your run() needs leds
    """
    return _TrinkeyLEDs()
