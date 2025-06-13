import board
import neopixel

def setup() -> neopixel.NeoPixel:
    return neopixel.NeoPixel(
        board.NEOPIXEL,
        1,
        brightness=0.1
    )
