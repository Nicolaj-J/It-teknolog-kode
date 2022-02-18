from time import sleep, sleep_ms
from machine import Pin, PWM, ADC
servo1=PWM(Pin(22),freq=50)
servo2=PWM(Pin(23),freq=50)
joyx = ADC(Pin(32))
joyy = ADC(Pin(35))
joyp = ADC(Pin(34))
joyx.atten(ADC.ATTN_11DB)
joyx.width(ADC.WIDTH_12BIT)
joyy.atten(ADC.ATTN_11DB)
joyy.width(ADC.WIDTH_12BIT)
joyp.atten(ADC.ATTN_11DB)
joyp.width(ADC.WIDTH_12BIT)
servomax = 90
servomin = 20
servonorm = 90
i = 80
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
        sleep_ms(100)
        if(x >= 1875-50):
            while(i >= servomin and i <= servomax and x >= 1875-50):
                x = joyx.read()
                servo1.duty(i)
                i = i - 1
                sleep_ms(100)
        if(x <= 1875+50):
            print("inde i +x")
            while(i >= servomin and i <= servomax and x <= 1875+50):
                x = joyx.read()
                servo1.duty(i)
                i = i + 1
                sleep_ms(100)
elif(besked == "servo"):
    stat = 0
    while(True):
        sleep_ms(100)
        print("1")
        if(stat == 1):
            print("3")
            while(i >= servomin):
                servo1.duty(i)
                i = i - 1
                sleep_ms(10)
                if(i == servomin):
                    stat = 0
        if(stat == 0):
            print("2")
            while(i <= servomax):
                servo1.duty(i)
                i = i + 1
                sleep_ms(10)
                if(i == servomax):
                    stat = 1
