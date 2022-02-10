from hcsr04 import HCSR04
from time import sleep
from machine import Pin, ADC, PWM
# hc-sr05 pins for ESP32
sensor = HCSR04(trigger_pin=5, echo_pin=18, echo_timeout_us=10000)
motor = PWM(Pin(4), 5000)
x = 0
pot = ADC(x)
pot.atten(ADC.ATTN_11DB)
pot.width(ADC.WIDTH_12BIT)
listeven = []
listehøj = []
listeavg = []
avgv = 0
avgh = 0
avg = 0
while True:
    x = 1000
    motor.duty(pot)
    print(motor.duty())
    x = 5000
    sleep(1)
    motor.duty(pot)
    print(motor.duty())
#     distance = sensor.distance_cm()
#     listeven.append(distance)
#     listehøj.append(10)
#     sleep(1)
#     avgv = sum(listeven)/len(listeven)
#     avgh = sum(listehøj)/len(listehøj)
#     print("avgv: ", avgv)
#     print("avgh: ", avgh)
#     if(len(listeven) >= 10 and len(listehøj) >= 10):
#         listeven.clear()
#         listehøj.clear()
#     avg = avgv - avgh
#     listeavg.append(avg)
#     print("avg: ", avg)
#     if(len(listeavg) == 10):
#         listeavg.pop(9)
#     print(len(listeavg))




