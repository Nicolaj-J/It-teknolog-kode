from time import sleep, sleep_ms
from machine import Pin, PWM, ADC
import joystickstyring
import _thread
servo4=PWM(Pin(""),freq=50) #Indtast pin
joy2y = ADC(Pin(35))
joy2y.atten(ADC.ATTN_11DB)
joy2y.width(ADC.WIDTH_12BIT)

class Servo4Stat:
    servomax = 120
    servomin = 75
    servonorm = 75
    hastighed = 100
    joystickmin = 1700
    joystickmax = 2100

def Joystick1yRead():
       y = joy2y.read()
       return y

def Servo4():
    servo4.duty(Servo4Stat.servonorm)
    check = joystickstyring.JoystickStyring("check")
    while(check == True):
        check = joystickstyring.JoystickStyring("check")
        y = Joystick1yRead()
        print("y2: ", y)
        sleep(1)
        if(y <= Servo4Stat.joystickmin):
            while(i >= Servo4Stat.servo4min and y <= Servo4Stat.joystickmin and check == True):
                check = joystickstyring.JoystickStyring("check")
                y = Joystick1yRead()
                servo4.duty(i)
                i = i - 1
                sleep_ms(Servo4Stat.hastighed)
        if(y >= Servo4Stat.joystickmax): 
            while(Servo4Stat.servo4max and y >= Servo4Stat.joystickmax and check == True):
                check = joystickstyring.JoystickStyring("check")
                y = Joystick1yRead()
                servo4.duty(i)
                i = i + 1
                sleep_ms(Servo4Stat.hastighed)