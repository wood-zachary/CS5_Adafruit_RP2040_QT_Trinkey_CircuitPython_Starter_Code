"""Collection of abstract classes for use reference.

(For students: don't worry about the code that's in here.
These classes are just providing examples of how to use the sensors and controllers.
The actual implementations of the classes are on the device.)
"""

class ProximitySensor:
    """Abstract proximity sensor."""

    @property
    def proximity(self) -> int:
        """
        Measured proximity, 0–255 (low = far, high = near).
        Example:
            prox = apds.proximity
        """
        raise NotImplementedError

class LEDController:
    """Abstract LED controller."""

    def fill(self, color: tuple[int, int, int]) -> None:
        """
        Set all LEDs to the given RGB color.
        Args:
            color: (r, g, b) each 0–255.
        Example:
            leds.fill((0,0,0))  # turn off
        """
        raise NotImplementedError

class TouchSensor:
    """Abstract touch sensor."""

    @property
    def value(self) -> bool:
        """
        True if being touched.
        Example:
            if touch.value: …
        """
        raise NotImplementedError

    @property
    def raw_value(self) -> int:
        """
        Raw capacitance reading.
        Example:
            raw = touch.raw_value
        """
        raise NotImplementedError

class NunchukController:
    """Abstract Wii Nunchuk interface."""

    @property
    def joystick(self) -> tuple[int, int]:
        """(x, y) joystick, 0–255 each."""
        raise NotImplementedError

    @property
    def acceleration(self) -> tuple[float, float, float]:
        """(ax, ay, az) accelerometer as floats."""
        raise NotImplementedError

    @property
    def buttons(self) -> object:
        """
        Button state object with attributes:
          C: bool
          Z: bool
        Example:
            if nunchuk.buttons.C: …
        """
        raise NotImplementedError

class MiniGamepad:
    """Abstract I2C mini gamepad (Seesaw-based)."""

    @property
    def x(self) -> int:
        """Joystick X axis (0–1023)."""
        raise NotImplementedError

    @property
    def y(self) -> int:
        """Joystick Y axis (0–1023)."""
        raise NotImplementedError

    @property
    def button_a(self) -> bool:
        """True if A pressed."""
        raise NotImplementedError

    @property
    def button_b(self) -> bool:
        """True if B pressed."""
        raise NotImplementedError

    @property
    def button_x(self) -> bool:
        """True if X pressed."""
        raise NotImplementedError

    @property
    def button_y(self) -> bool:
        """True if Y pressed."""
        raise NotImplementedError

    @property
    def button_start(self) -> bool:
        """True if Start pressed."""
        raise NotImplementedError

    @property
    def button_select(self) -> bool:
        """True if Select pressed."""
        raise NotImplementedError