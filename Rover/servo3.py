from time import sleep, sleep_ms
from machine import Pin, PWM, ADC
import joystickstyring
import _thread
servo3=PWM(Pin(""),freq=50) #Indtast pin
joy2x = ADC(Pin(33))
joy2x.atten(ADC.ATTN_11DB)
joy2x.width(ADC.WIDTH_12BIT)

class Servo3Stat:
    servomax = 120
    servomin = 75
    servonorm = 75
    hastighed = 100
    joystickmin = 1700
    joystickmax = 2100

def Joystick2xRead():
       x = joy2x.read()
       return x

def Servo3():
    servo3.duty(Servo3Stat.servonorm)
    check = joystickstyring.JoystickStyring("check")
    while(check == True):
        check = joystickstyring.JoystickStyring("check")
        x = Joystick2xRead()
        print("x2: ", x)
        sleep(1)
        if(x <= Servo3Stat.joystickmin):
            while(i >= Servo3Stat.servo3min and x <= Servo3Stat.joystickmin and check == True):
                check = joystickstyring.JoystickStyring("check")
                x = Joystick2xRead()
                servo3.duty(i)
                i = i - 1
                sleep_ms(Servo3Stat.hastighed)
        if(x >= Servo3Stat.joystickmax): 
            while(Servo3Stat.servo3max and x >= Servo3Stat.joystickmax and check == True):
                check = joystickstyring.JoystickStyring("check")
                x = Joystick2xRead()
                servo3.duty(i)
                i = i + 1
                sleep_ms(Servo3Stat.hastighed)