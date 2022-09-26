import time
import motorstyring
import _thread
from machine import Pin
buzzer = Pin(32, Pin.OUT, value=0)
class Joystickconstat:
    joystickMid = 2048
    deadzoneMin = 1700
    deadzoneMax = 2100
    joystickxreading = 2048
    joystickyreading = 2048
    joystickconversionoption = False
    minspeedvalue = 300

def Conversion():
    print("tråd startet")
    check = Joystickconstat.joystickconversionoption
    while(True):
        check = Joystickconstat.joystickconversionoption
        if(check == False):
            _thread.exit()
            break
        measurementx = Joystickconstat.joystickxreading
        measurementy = Joystickconstat.joystickyreading
        pwmMvalue = Joystickconstat.joystickMid / 750
        measurementx = measurementx - 2048
        measurementy = measurementy - 2048

        if(measurementx > 0 and motorstyring.Motorstat.vdirection != 0 and motorstyring.Motorstat.hdirection != 0):
            motorstyring.Motorstat.vdirection = 0
            motorstyring.Motorstat.hdirection = 0
            buzzer.value(1)
        elif(measurementx < 0 and motorstyring.Motorstat.vdirection != 1 and motorstyring.Motorstat.hdirection != 1):
            motorstyring.Motorstat.vdirection = 1
            motorstyring.Motorstat.hdirection = 1
            buzzer.value(0)

        if(measurementy < 0):

            pwmVvalue = abs(measurementx)/pwmMvalue
            pwmHvalue = (1-(abs(measurementy)/2048))*pwmVvalue
        elif(measurementy > 0):

            pwmHvalue = abs(measurementx)/pwmMvalue
            pwmVvalue = (1-(abs(measurementy)/2048))*pwmHvalue
        elif(measurementy == 0):

            pwmVvalue = abs(measurementx)/pwmMvalue
            pwmHvalue = abs(measurementx)/pwmMvalue


        if(pwmHvalue < Joystickconstat.minspeedvalue):
            if(pwmHvalue > Joystickconstat.minspeedvalue - 150 and pwmHvalue < 300):
                pwmHvalue = 300
            if(pwmHvalue <= Joystickconstat.minspeedvalue - 150):
                pwmHvalue = 0
        pwmhsend = abs(pwmHvalue)
        motorstyring.Motorstat.hspeed = int(pwmhsend)
        if(pwmVvalue < Joystickconstat.minspeedvalue):
            if(pwmVvalue > Joystickconstat.minspeedvalue - 150 and pwmVvalue < 300):
                pwmVvalue = 300
            if(pwmVvalue <= Joystickconstat.minspeedvalue - 150):
                pwmVvalue = 0
        pwmvsend = abs(pwmVvalue)
        motorstyring.Motorstat.vspeed = int(pwmvsend)
        #print("pwmH: ", pwmhsend, "---", "pwmV: ", pwmvsend)
        measurementx = 0
        measurementy = 0

