from earsketch import *

def setup():
    init()
    setTempo(72)  # Slower, more traditional carol tempo

def create_christmas_carol():
    # Traditional carol instrumentation
    piano = COMMON_LOVE_THEME_PIANO_1            # Main melody instrument
    strings = COMMON_LOVE_THEME_STRINGS_1        # Orchestral strings
    choir = YG_TRAP_SYNTH_CHOIR_1            # Backing choir sounds

    # Traditional 4/4 carol patterns
    melody_accomp = "0---0---0---0---"    # Basic accompaniment
    choir_pattern = "0-------0-------"     # Long choir notes

    # INTRODUCTION (Measures 1-8)
    fitMedia(piano, 1, 1, 8)
    setEffect(1, VOLUME, GAIN, -15, 1, -5, 8)  # Fade in piano

    # FIRST VERSE (Measures 9-24)
    fitMedia(piano, 1, 9, 24)
    fitMedia(strings, 2, 9, 24)

    # CHORUS (Measures 25-40)
    fitMedia(piano, 1, 25, 40)
    fitMedia(strings, 2, 25, 40)
    fitMedia(choir, 3, 25, 40)

    # BRIDGE (Measures 41-48)
    fitMedia(piano, 1, 41, 48)
    fitMedia(strings, 2, 41, 48)
    fitMedia(choir, 3, 41, 48)

    # FINAL CHORUS (Measures 49-64)
    fitMedia(piano, 1, 49, 64)
    fitMedia(strings, 2, 49, 64)
    fitMedia(choir, 3, 49, 64)

    # Volume balance for traditional carol feel
    setEffect(1, VOLUME, GAIN, -5)     # Piano
    setEffect(2, VOLUME, GAIN, -8)     # Strings
    setEffect(3, VOLUME, GAIN, -7)     # Choir

    # Dynamic swells for emotional impact
    setEffect(2, VOLUME, GAIN, -12, 25, -6, 32)  # String swell
    setEffect(3, VOLUME, GAIN, -10, 25, -5, 32)  # Choir swell

def main():
    setup()
    create_christmas_carol()
    finish()

main()
