from time import sleep, sleep_ms
from machine import Pin, PWM, ADC
import _thread

class Servo2Stat:
    servomax = 75
    servomin = 48
    servonorm = 48
    hastighed = 100
    joystickmeasurement = 2048
    joystickmax = 2100
    joystickmin = 1700
    servooption = False

def Servo2():

    servo2=PWM(Pin(22),freq=50)
    servo2.duty(Servo2Stat.servonorm)
    check = Servo2Stat.servooption
    while(check == True):
        
        check = Servo2Stat.servooption
        y = Servo2Stat.joystickmeasurement
        sleep(1)

        if(y <= Servo2Stat.joystickmin):
            while(i >= Servo2Stat.servomin and y <= Servo2Stat.joystickmin and check == True):
                check = Servo2Stat.servooption
                y = Servo2Stat.joystickmeasurement
                servo2.duty(i)

                i = i - 1
                sleep_ms(Servo2Stat.hastighed)
        if(y >= Servo2Stat.joystickmax):
            while(Servo2Stat.servomax and y >= Servo2Stat.joystickmax and check == True):
                check = Servo2Stat.servooption
                y = Servo2Stat.joystickmeasurement
                servo2.duty(i)

                i = i + 1
                sleep_ms(Servo2Stat.hastighed)
