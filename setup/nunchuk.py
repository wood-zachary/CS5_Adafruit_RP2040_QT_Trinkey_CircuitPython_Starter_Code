import board
import time
from adafruit_nunchuk import Nunchuk

def setup() -> Nunchuk:
    """
    Returns a Wiinunchuk instance (implements Wiinunchuk)
    via the adafruit_nunchuk library on STEMMA_I2C().
    """
    i2c = board.STEMMA_I2C()
    nunchuk  = Nunchuk(i2c, address=0x52)
    time.sleep(0.01)
    return nunchuk
