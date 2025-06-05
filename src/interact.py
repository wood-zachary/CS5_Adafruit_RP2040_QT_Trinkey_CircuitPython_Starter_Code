from .abstract import LEDController
# from .pulse import run_simple_pulse
from .macros import run_macros

'''
Always comment out any imports you're not using to save memory.
'''

def run(pixels: LEDController):
    """
    Runs the selected demo on the Trinkey.

    Args:
        potentiometer: AnalogSlider
        touch: TouchSensor
        pixels: LEDController
    """
    # run_simple_pulse(pixels)
    run_macros(pixels)
