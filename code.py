try:
    import board
except ModuleNotFoundError:
    pass
else:
    from src.drivers.rp2040_qt_trinkey import make_rp2040_qt_trinkey_devices
    from src.interact import run

    # Setup board
    pixels = make_rp2040_qt_trinkey_devices()
    print("Loaded Trinkey...")

    # Call our run function
    run(pixels)
