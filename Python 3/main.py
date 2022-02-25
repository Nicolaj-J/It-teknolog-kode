import Relæ
import _thread
from time import sleep_ms
from machine import Pin
knap = Pin(25, Pin.IN)
while True:
    sleep_ms(500)
    besked = input()
    if besked == "tilbage":
        Relæ.motor_styring("tilbage")
        besked = ""
    if besked == "frem":
        Relæ.motor_styring("frem")
        besked = ""
