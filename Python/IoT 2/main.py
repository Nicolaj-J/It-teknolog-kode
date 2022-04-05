from gpiozero import Button
import dbConverter
import time
import capture

button = Button(16) #laver en instance af knap klassen til pin 16

def interrupt():        #definere en funktion der hedder interrupt
    print("button pressed")
    dbConverter.start(capture.barcode_read())       #Kørerrrrrrr start funktionen i dbconverter med et argumentet som barcode_read returnererrrrrrrrrrr

button.when_pressed = interrupt #Definerer hvilken funktion der skal køres når knappen trykkes

while True:                     #dette while loop er her koden venter indtil der trykkes
    time.sleep(0.5)