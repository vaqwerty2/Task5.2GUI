import tkinter as tk
from gpiozero import PWMLED

# Setup your PWMLEDs with GPIO pins
led1 = PWMLED(17)  # Change '17' to your GPIO pin connected to the first LED
led2 = PWMLED(27)  # Change '27' to your GPIO pin connected to the second LED
led3 = PWMLED(22)  # Change '22' to your GPIO pin connected to the third LED

def update_led1(value):
    """ Update the brightness of the first LED based on the slider's position. """
    led1.value = float(value) / 100.0

def update_led2(value):
    """ Update the brightness of the second LED based on the slider's position. """
    led2.value = float(value) / 100.0

def update_led3(value):
    """ Update the brightness of the third LED based on the slider's position. """
    led3.value = float(value) / 100.0

# Create the main window
root = tk.Tk()
root.title("LED Brightness Controller")

# Create sliders for brightness control of each LED
slider1 = tk.Scale(root, from_=0, to=100, orient='horizontal', label='LED 1 Brightness', command=update_led1)
slider1.pack()
slider2 = tk.Scale(root, from_=0, to=100, orient='horizontal', label='LED 2 Brightness', command=update_led2)
slider2.pack()
slider3 = tk.Scale(root, from_=0, to=100, orient='horizontal', label='LED 3 Brightness', command=update_led3)
slider3.pack()

# Start the GUI event loop
root.mainloop()
