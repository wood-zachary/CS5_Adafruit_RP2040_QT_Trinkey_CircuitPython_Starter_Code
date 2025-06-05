"""Collection of abstract classes for type hinting in the rest of the project.

(For students: don't worry about the code that's in here.
These classes are just providing examples of how to use the sensors
and other peripherals for type hinting.
The actual implementations of the classes are on the device.)
"""
# We aren't using the abc module because it isn't available on circuitpy.

# When making a project, remove any abstract classes you aren't using. 
# The boards do not have enough memory to handle dozens of abstract classes.

class LEDController:
    """Abstract LED controller."""

    def fill(self, color: tuple[int, int, int]) -> None:
        """Change the color of the LED being controlled.

        Args:
            color: Three-tuple of integers in [0, 255] representing the values
                of red, green, and blue to display on the LED.

        Example:
            `px.fill((0, 0, 0))` turns the LED off
        """
        raise NotImplementedError