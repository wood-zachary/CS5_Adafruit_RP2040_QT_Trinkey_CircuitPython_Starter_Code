import board
from src.interact import run

try:
    from setup.nunchuk import setup as _setup_nunchuk
    nunchuk = _setup_nunchuk()
    print("Loaded Nunchuk")
except Exception as e:
    nunchuk = None
    print(f"Skipping Nunchuk: {e!r}")

try:
    from setup.minigamepad import setup as _setup_minigamepad
    gamepad = _setup_minigamepad()
    print("Loaded MiniGamepad")
except Exception as e:
    gamepad = None
    print(f"Skipping MiniGamepad: {e!r}")

try:
    from setup.rp2040_qt_trinkey import setup as _setup_leds
    pixels = _setup_leds()
    print("Loaded Trinkey LEDs")
except Exception as e:
    pixels = None
    print(f"Skipping Trinkey LEDs: {e!r}")

try:
    from setup.apds9960 import setup as _setup_apds
    apds, pixels, touch1, touch2 = _setup_apds()
    print("Loaded APDS9960 + LEDs + Touch")
except Exception as e:
    try:
        pixels
    except: 
        pixels = None
    apds = touch1 = touch2 = None
    print(f"Skipping APDS9960 suite: {e!r}")


run(
    apds=apds,
    pixels=pixels,
    touch1=touch1,
    touch2=touch2,
    nunchuk=nunchuk,
    gamepad=gamepad,
)