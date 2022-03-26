from gpiozero import Button
import dbConverter
import time
import capture

button = Button(16)

def interrupt():
    print("button pressed")
    dbConverter.start(capture.barcode_read())

button.when_pressed = interrupt

while True:
    time.sleep(0.5)