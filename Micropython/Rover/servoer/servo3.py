from time import sleep, sleep_ms
from machine import Pin, PWM, ADC
import _thread

class Servo3Stat:
    servomax = 90
    servomin = 70
    servonorm = 75
    hastighed = 50
    joystickmeasurement = 2048
    joystickmax = 2100
    joystickmin = 1700
    servooption = False

def Servo3():

    servo3=PWM(Pin(21),freq=50)
    servo3.duty(Servo3Stat.servonorm)
    check = Servo3Stat.servooption
    i = Servo3Stat.servonorm
    print("servo3 startet")
    while(True):
        sleep_ms(int(Servo3Stat.hastighed))
        check = Servo3Stat.servooption
        if(check == False):
            _thread.exit()
            break
        y = int(Servo3Stat.joystickmeasurement)
        # print("servo3 ", Servo3Stat.joystickmeasurement)
        if(int(y) <= int(Servo3Stat.joystickmin)):
            while(i > Servo3Stat.servomin and y <= Servo3Stat.joystickmin and check == True):
                check = Servo3Stat.servooption
                y = int(Servo3Stat.joystickmeasurement)
                servo3.duty(i)
                print("servo 3", i)
                i = i - 1
                sleep_ms(Servo3Stat.hastighed)
        if(y >= int(Servo3Stat.joystickmax)):
            while(i < Servo3Stat.servomax and y >= Servo3Stat.joystickmax and check == True):
                check = Servo3Stat.servooption
                y = int(Servo3Stat.joystickmeasurement)
                print("servo 3", i)
                servo3.duty(i)
                i = i + 1
                sleep_ms(Servo3Stat.hastighed)
    _thread.exit()
