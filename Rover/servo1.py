from time import sleep, sleep_ms
from machine import Pin, PWM, ADC
import joystickstyring
import _thread
servo1=PWM(Pin(""),freq=50) #Indtast pin
joy1x = ADC(Pin(34))
joy1x.atten(ADC.ATTN_11DB)
joy1x.width(ADC.WIDTH_12BIT)

class Servo1Stat:
    servomax = 120
    servomin = 75
    servonorm = 75
    hastighed = 100
    joystickmin = 1700
    joystickmax = 2100
    
def Joystick1xRead():
       x = joy1x.read()
       return x

def Servo1():
    servo1.duty(Servo1Stat.servonorm)
    check = joystickstyring.JoystickStyring("check")
    while(check == True):
        check = joystickstyring.JoystickStyring("check")
        x = Joystick1xRead()
        print("x1: ", x)
        sleep(1)
        if(x <= Servo1Stat.joystickmin):
            while(i >= Servo1Stat.servomin and x <= Servo1Stat.joystickmin and check == True):
                check = joystickstyring.JoystickStyring("check")
                x = Joystick1xRead()
                servo1.duty(i)
                i = i - 1
                sleep_ms(Servo1Stat.hastighed)
        if(x >= Servo1Stat.joystickmax): 
            while(Servo1Stat.servomax and x >= Servo1Stat.joystickmax and check == True):
                check = joystickstyring.JoystickStyring("check")
                x = Joystick1xRead()
                servo1.duty(i)
                i = i + 1
                sleep_ms(Servo1Stat.hastighed)