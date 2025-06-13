import time
import board
from adafruit_seesaw.seesaw import Seesaw
from src.abstract import MiniGamepad

_DEFAULT_ADDRESS = 0x50

_BUTTON_MASK = (
    (1 << 6)   |  # X
    (1 << 2)   |  # Y
    (1 << 5)   |  # A
    (1 << 1)   |  # B
    (1 << 0)   |  # Select
    (1 << 16)     # Start
)

class _SeesawGamepad(MiniGamepad):
    def __init__(self, seesaw: Seesaw):
        self._ss = seesaw

    @property
    def x(self) -> int:
        return 1023 - self._ss.analog_read(14)

    @property
    def y(self) -> int:
        return 1023 - self._ss.analog_read(15)

    def _buttons(self) -> int:
        return self._ss.digital_read_bulk(_BUTTON_MASK)

    @property
    def button_a(self) -> bool:
        return not bool(self._buttons() & (1 << 5))

    @property
    def button_b(self) -> bool:
        return not bool(self._buttons() & (1 << 1))

    @property
    def button_x(self) -> bool:
        return not bool(self._buttons() & (1 << 6))

    @property
    def button_y(self) -> bool:
        return not bool(self._buttons() & (1 << 2))

    @property
    def button_start(self) -> bool:
        return not bool(self._buttons() & (1 << 16))

    @property
    def button_select(self) -> bool:
        return not bool(self._buttons() & (1 << 0))

def setup() -> MiniGamepad:
    i2c    = board.STEMMA_I2C()
    seesaw = Seesaw(i2c, addr=_DEFAULT_ADDRESS)
    seesaw.pin_mode_bulk(_BUTTON_MASK, seesaw.INPUT_PULLUP)
    time.sleep(0.01)
    return _SeesawGamepad(seesaw)
