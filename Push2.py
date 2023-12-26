import push2_python
import cairo
import numpy
import random
import time


import usb.core
import usb.util
from usb.backend import libusb1
import platform
import os
# Get the directory where the current script is located
current_dir = os.path.dirname(os.path.realpath(__file__))

# Construct the path to the 'libusb-1.0.dll' in the current directory
libusb_path = os.path.join(current_dir, 'libusb-1.0.dll')

# Set the backend to use the specific 'libusb-1.0.dll'
backend = usb.backend.libusb1.get_backend(find_library=lambda x: libusb_path)

# Init Push2
push = push2_python.Push2()

def LightItUpButtons():
    push.buttons.set_button_color("Add Track", 'white')  # Adjust color as needed
    push.buttons.set_button_color("Mute", 'white')  # Adjust color as needed
    push.buttons.set_button_color("Fixed Length", 'white')  # Adjust color as needed
    push.buttons.set_button_color("Shift", 'white')  # Adjust color as needed
    push.buttons.set_button_color("Lower Row 3", 'white')  # Adjust color as needed
    push.buttons.set_button_color("Quantize", 'white')  # Adjust color as needed
    push.buttons.set_button_color("1/8t", 'white')  # Adjust color as needed
    push.buttons.set_button_color("Metronome", 'white')  # Adjust color as needed

    push.buttons.set_button_color("Solo", 'white')  # Adjust color as needed
    push.buttons.set_button_color("Automate", 'white')  # Adjust color as needed
    push.buttons.set_button_color("Lower Row 1", 'white')  # Adjust color as needed
    push.buttons.set_button_color("1/32", 'white')  # Adjust color as needed
    push.buttons.set_button_color("Device", 'white')  # Adjust color as needed
    push.buttons.set_button_color("Accent", 'white')  # Adjust color as needed
    push.buttons.set_button_color("Convert", 'white')  # Adjust color as needed
    push.buttons.set_button_color("Session", 'white')  # Adjust color as needed
    push.buttons.set_button_color("Upper Row 6", 'white')  # Adjust color as needed
    push.buttons.set_button_color("Lower Row 6", 'white')  # Adjust color as needed

    push.buttons.set_button_color("1/4", 'white')  # Adjust color as needed
    push.buttons.set_button_color("Clip", 'white')  # Adjust color as needed
    push.buttons.set_button_color("Delete", 'white')  # Adjust color as needed
    push.buttons.set_button_color("Lower Row 8", 'white')  # Adjust color as needed
    push.buttons.set_button_color("Mix", 'white')  # Adjust color as needed
    push.buttons.set_button_color("User", 'white')  # Adjust color as needed
    push.buttons.set_button_color("Upper Row 5", 'white')  # Adjust color as needed
    push.buttons.set_button_color("Upper Row 4", 'white')  # Adjust color as needed
    push.buttons.set_button_color("Lower Row 5", 'white')  # Adjust color as needed
    push.buttons.set_button_color("Browse", 'white')  # Adjust color as needed
    push.buttons.set_button_color("Repeat", 'white')  # Adjust color as needed
    push.buttons.set_button_color("Lower Row 4", 'white')  # Adjust color as needed
    push.buttons.set_button_color("Play", 'white')  # Adjust color as needed
    push.buttons.set_button_color("Note", 'white')  # Adjust color as needed
    push.buttons.set_button_color("Down", 'white')  # Adjust color as needed
    push.buttons.set_button_color("Select", 'white')  # Adjust color as needed
    push.buttons.set_button_color("Right", 'white')  # Adjust color as needed
    push.buttons.set_button_color("Lower Row 7", 'white')  # Adjust color as needed
    push.buttons.set_button_color("Upper Row 8", 'white')  # Adjust color as needed
    push.buttons.set_button_color("Left", 'white')  # Adjust color as needed
    push.buttons.set_button_color("Stop", 'white')  # Adjust color as needed
    push.buttons.set_button_color("Setup", 'white')  # Adjust color as needed
    push.buttons.set_button_color("1/32t", 'white')  # Adjust color as needed
    push.buttons.set_button_color("1/4t", 'white')  # Adjust color as needed
    push.buttons.set_button_color("1/8", 'white')  # Adjust color as needed
    push.buttons.set_button_color("Undo", 'white')  # Adjust color as needed
    push.buttons.set_button_color("1/16t", 'white')  # Adjust color as needed
    push.buttons.set_button_color("Upper Row 2", 'white')  # Adjust color as needed
    push.buttons.set_button_color("Upper Row 3", 'white')  # Adjust color as needed
    push.buttons.set_button_color("Master", 'white')  # Adjust color as needed
    push.buttons.set_button_color("1/16", 'white')  # Adjust color as needed
    push.buttons.set_button_color("Upper Row 1", 'white')  # Adjust color as needed
    push.buttons.set_button_color("Scale", 'white')  # Adjust color as needed
    push.buttons.set_button_color("Double Loop", 'white')  # Adjust color as needed
    push.buttons.set_button_color("Tap Tempo", 'white')  # Adjust color as needed
    push.buttons.set_button_color("Record", 'white')  # Adjust color as needed
    push.buttons.set_button_color("Up", 'white')  # Adjust color as needed
    push.buttons.set_button_color("Lower Row 2", 'white')  # Adjust color as needed
    push.buttons.set_button_color("Layout", 'white')  # Adjust color as needed
    push.buttons.set_button_color("Duplicate", 'white')  # Adjust color as needed
    push.buttons.set_button_color("New", 'white')  # Adjust color as needed
    push.buttons.set_button_color("Upper Row 7", 'white')  # Adjust color as needed
    push.buttons.set_button_color("Add Device", 'white')  # Adjust color as needed

    push.buttons.set_button_color("Page Left", 'white')  # Adjust color as needed
    push.buttons.set_button_color("Page Right", 'white')  # Adjust color as needed
    push.buttons.set_button_color("Octave Down", 'white')  # Adjust color as needed
    push.buttons.set_button_color("Octave Up", 'white')  # Adjust color as needed
    