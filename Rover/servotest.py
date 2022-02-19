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
servo1min = 110
servo1norm = 90
servo2max = 100
servo2min = 40
servo2norm = 90
i = 110
servo1.duty(110)
x = joyx.read()
y = joyy.read()
p = joyp.read()/4095
print("x: ", joyx.read())
print("y: ", joyy.read())
print("p: ", (joyp.read()/4095) )
print("skriv 'joystick' for joystick test eller 'servo' for servo test")
besked = "servo"
if(besked == "joystick"):
    while(True):
        x = joyx.read()
        print("x1: ",x)
        sleep_ms(100)
        if(x <= 1700):
            while(i >= servo1min and x <= 1875-50):
                x = joyx.read()
                print("x2: ",x)
                servo1.duty(i)
                i = i - 1
                sleep_ms(10)
        if(x >= 2100): 
            while(servo1max and x >= 1875+50):
                x = joyx.read()
                print("x3: ",x)
                servo1.duty(i)
                i = i + 1
                sleep_ms(10)
elif(besked == "servo"):
    stat = 0
    while(True):
        sleep_ms(100)
        print("1")
        if(stat == 1):
            print("3")
            while(i >= servo1min):
                servo1.duty(i)
                i = i - 1
                sleep_ms(10)
                if(i == servo1min):
                    stat = 0
        if(stat == 0):
            print("2")
            while(i <= servo1max):
                servo1.duty(i)
                i = i + 1
                sleep_ms(10)
                if(i == servo1max):
                    stat = 1
