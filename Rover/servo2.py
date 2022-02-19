from time import sleep, sleep_ms
from machine import Pin, PWM, ADC
import joystickstyring
import _thread
servo2=PWM(Pin(""),freq=50) #Indtast
joy1y = ADC(Pin(39))
joy1y.atten(ADC.ATTN_11DB)
joy1y.width(ADC.WIDTH_12BIT)

class Servo2Stat:
    servomax = 120
    servomin = 75
    servonorm = 75
    hastighed = 100
    joystickmin = 1700
    joystickmax = 2100

def Joystick1yRead():
       y = joy1y.read()
       return y

def Servo2():
    servo2.duty(Servo2Stat.servonorm)
    check = joystickstyring.JoystickStyring("check")
    while(check == True):
        check = joystickstyring.JoystickStyring("check")
        y = Joystick1yRead()
        print("y1: ", y)
        sleep(1)
        if(y <= Servo2Stat.joystickmin):
            while(i >= Servo2Stat.servo2min and y <= Servo2Stat.joystickmin and check == True):
                check = joystickstyring.JoystickStyring("check")
                y = Joystick1yRead()
                servo2.duty(i)
                i = i - 1
                sleep_ms(Servo2Stat.hastighed)
        if(y >= Servo2Stat.joystickmax): 
            while(Servo2Stat.servo2max and y >= Servo2Stat.joystickmax and check == True):
                check = joystickstyring.JoystickStyring("check")
                y = Joystick1yRead()
                servo2.duty(i)
                i = i + 1
                sleep_ms(Servo2Stat.hastighed)