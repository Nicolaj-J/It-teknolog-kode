from time import sleep, sleep_ms
from machine import Pin, PWM, ADC
servo1=PWM(Pin(22),freq=50)
servo2=PWM(Pin(23),freq=50)
joyx = ADC(Pin(35))
joyp = ADC(Pin(32))
joyy = ADC(Pin(33))
joyx.atten(ADC.ATTN_11DB)
joyx.width(ADC.WIDTH_12BIT)
joyy.atten(ADC.ATTN_11DB)
joyy.width(ADC.WIDTH_12BIT)
joyp.atten(ADC.ATTN_11DB)
joyp.width(ADC.WIDTH_12BIT)
servo1max = 120
servo1min = 20
servo1norm = 90
servo2max = 100
servo2min = 40
servo2norm = 90
i = 70
servo1.duty(90)
