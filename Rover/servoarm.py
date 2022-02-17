from time import sleep, sleep_ms
from machine import Pin, PWM, ADC
import _thread
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
servomax = 120
servomin = 20
servonorm = 70
i = servonorm
has = 0
def joystick():
    while(True):
        sleep(0.5)
        print("x: ", joyx.read())
        print("y: ", joyy.read())
        print("p: ", (joyp.read()/4095) )
        x = joyx.read()
        y = joyy.read()
        p = joyp.read()/4095


def servostyringx(): 
    while(True):
        global x
        print("over if")
        if(x >= 1875-50):
            print("inde i -x")
            while(i >= servomin and i <= servomax):
                servo1.duty(i)
                i = i - 1
                sleep(2048/x)
        if(x <= 1875+50):
            print("inde i +x")
            while(i >= servomin and i <= servomax):
                servo1.duty(i)
                i = i + 1
                sleep(2048/x)
_thread.start_new_thread(servostyringx, ())
_thread.start_new_thread(joystick, ()) 
    # if(x == "v"):
    #     for i in range(servomin,servomax,1):
    #         servo.duty(i)
    #         sleep_ms(20)
    # if(x == "h"):
    #     for i in range(servomax,servomin,-1):
    #         servo.duty(i)
    #         sleep_ms(20)
    # if(x == "reset"):
    #     servo.duty(70)
    # sleep_ms(100)