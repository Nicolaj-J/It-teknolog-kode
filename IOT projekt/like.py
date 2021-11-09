from machine import Pin
import neopixel
import time
import tm1637
tm = tm1637.TM1637(clk=Pin(2), dio=Pin(0))

# import umqtt_robust2
# lib = umqtt_robust2
n = 12
p = 15
np = neopixel.NeoPixel(Pin(p), n)
tidl = 0

def tid_like(tid):
    tidl = tid

def likes(r, g, b):
    for i in range(n):
        np[i] = (r, g, b)
    np.write()
    time.sleep(0.5)
    for i in range(n):
        np[i] = (0,0,0)
        np.write()

# def clear():
#     for i in range(n):
#         np[i] = (0,0,0)
#         np.write()

def likes_count(likes):
    tm.brightness(6)
    tm.number(int(likes))
    print(likes)

def start_up():
    for i in range(n):
        np[i] = (0,0,0)
        np.write()
    tm.number(0)




