from neopixel import NeoPixel
from .abstract import MiniGamepad
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode 
from support.mytyping import NoReturn

def run_gamepad_space_macro(gamepad: MiniGamepad, pixels: NeoPixel) -> NoReturn:
    INTERVAL = 0.05
    GREEN = ((0, 150, 0))
    YELLOW = ((75, 75, 0))

    kb_macro = Keycode.SPACE
    kb = Keyboard(usb_hid.devices) 
    pixels.fill(YELLOW)
    
    is_pressed = False
    
    while True:
        press = gamepad.button_a

        # Your Code Here!
        
        time.sleep(INTERVAL)