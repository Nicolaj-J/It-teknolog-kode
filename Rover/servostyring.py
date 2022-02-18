from time import sleep, sleep_ms
from machine import Pin, PWM, ADC
import servo1, servo2, servo3, servo4
import _thread
s1 = 0
s2 = 0
s3 = 0
s4 = 0

def servo1control(besked):
    print("servocontrol")
    if(besked == "check"):
        return s1
    if(besked == "start" and s1 != 1):
        s1 = 1
        _thread.start_new_thread(servo1.servo1styring, ())
    if(besked == "stop" and s1 != 0):
        s1 = 0
def servo2control(besked):
    if(besked == "check"):
        return s2
    if(besked == "start" and s2 != 1):
        s2 = 1
        _thread.start_new_thread(servo2.servo1styring, ())
    if(besked == "stop" and s2 != 0):
        s2 = 0
def servo3control(besked):
    if(besked == "check"):
        return s3
    if(besked == "start" and s3 != 1):
        s3 = 1
        _thread.start_new_thread(servo3.servo1styring, ())
    if(besked == "stop" and s3 != 0):
        s3 = 0
def servo4control(besked):
    if(besked == "check"):
        return s4
    if(besked == "start" and s4 != 1):
        s4 = 1
        _thread.start_new_thread(servo4.servo1styring, ())
    if(besked == "stop" and s4 != 0):
        s4 = 0
