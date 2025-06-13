from neopixel import NeoPixel
from adafruit_nunchuk import Nunchuk
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode 
from support.mytyping import NoReturn

def run_nunchuk_space_macro(nunchuk: Nunchuk, pixels: NeoPixel) -> NoReturn:
    """
    Press the space key with a component or peripheral of your Trinkey.
    
    Args:
        nunchuk (Nunchuk): Wii Nunchuk.
        pixels (NeoPixel): NeoPixel object.
    """
    INTERVAL = 0.05
    GREEN = ((0, 150, 0))
    YELLOW = ((75, 75, 0))

    kb_macro = Keycode.SPACE
    kb = Keyboard(usb_hid.devices) 
    pixels.fill(YELLOW)

    is_pressed = False
    
    while True:
        press = nunchuk.buttons.C

        # Your Code Here!
        
        time.sleep(INTERVAL)


