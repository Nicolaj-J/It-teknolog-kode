from machine import Pin, PWM
import _thread
rightEnable = Pin(14, Pin.OUT)
leftEnable = Pin(4, Pin.OUT)

leftFrontDirection = Pin(17, Pin.OUT)
leftBackDirection = Pin(0, Pin.OUT)
rightFrontDirection = Pin(27, Pin.OUT)
rightBackDirection =Pin(13, Pin.OUT)

leftFrontSpeed = PWM(Pin(16),freq=50)
leftBackSpeed = PWM(Pin(15),freq=50)
rightFrontSpeed = PWM(Pin(26),freq=50)
rightBackSpeed  = PWM(Pin(12),freq=50)

class Motorstat:
    hspeed = 0
    vspeed = 0
    hdirection = 0
    vdirection = 0
    motoroption = False



def h_motorer():
    check = Motorstat.motoroption
    while(True):
        check = Motorstat.motoroption
        if(check == False):
            _thread.exit()
            break
        if(Motorstat.hdirection == 0): #forlæns
                if(rightEnable.value() == 0):
                    rightEnable.value(1)
                rightFrontDirection.value(1)
                rightBackDirection.value(1)
                rightFrontSpeed.duty(int(Motorstat.hspeed))
                rightBackSpeed.duty(int(Motorstat.hspeed))
        elif(Motorstat.hdirection == 1): #baglæns
                if(rightEnable.value() == 0):
                    rightEnable.value(1)
                rightFrontDirection.value(0)
                rightBackDirection.value(0)
                rightFrontSpeed.duty(int(Motorstat.hspeed))
                rightBackSpeed.duty(int(Motorstat.hspeed))
        else:
            rightEnable.value(0)
    _thread.exit()

def v_motorer():
    checkv = Motorstat.motoroption
    while(checkv == True):
        checkv = Motorstat.motoroption
        if(Motorstat.vdirection == 1): #forlæns
                if(leftEnable.value() == 0):
                    leftEnable.value(1)
                leftFrontDirection.value(0)
                leftBackDirection.value(0)
                leftFrontSpeed.duty(int(Motorstat.vspeed))
                leftBackSpeed.duty(int(Motorstat.vspeed))
        elif(Motorstat.vdirection == 0): #baglæns
                if(leftEnable.value() == 0):
                    leftEnable.value(1)
                leftFrontDirection.value(1)
                leftBackDirection.value(1)
                leftFrontSpeed.duty(int(Motorstat.vspeed))
                leftBackSpeed.duty(int(Motorstat.vspeed))
        else:
            leftEnable.value(0)
    _thread.exit()








