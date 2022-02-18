from time import sleep, sleep_ms
from machine import ADC, Pin
joy1p = ADC(Pin(36))
joy1y = ADC(Pin(39))
joy1x = ADC(Pin(34))
joy2x = ADC(Pin(35))
joy2y = ADC(Pin(33))
joy2p = ADC(Pin(32))
joy1x.atten(ADC.ATTN_11DB)
joy1x.width(ADC.WIDTH_12BIT)
joy1y.atten(ADC.ATTN_11DB)
joy1y.width(ADC.WIDTH_12BIT)
joy1p.atten(ADC.ATTN_11DB)
joy1p.width(ADC.WIDTH_12BIT)
joy2x.atten(ADC.ATTN_11DB)
joy2x.width(ADC.WIDTH_12BIT)
joy2y.atten(ADC.ATTN_11DB)
joy2y.width(ADC.WIDTH_12BIT)
joy2p.atten(ADC.ATTN_11DB)
joy2p.width(ADC.WIDTH_12BIT)
# sleep(1)
# print("joystick 1 p: ", joy1p.read())
# print("joystick 1 x: ", joy1x.read())
# print("joystick 1 y: ", joy1y.read())
# print("joystick 2 p: ", joy2p.read())
# print("joystick 2 x: ", joy2x.read())
# print("joystick 2 y: ", joy2y.read())
def joy1måling(data):
    sleep_ms(10)
    if(data == "button"):
        p = joy1p.read()/4095
    if(data == "xakse"):
        x = joy1x.read()
    if(data == "yakse"):
        y = joy1y.read()   
    return p,x,y

def joy2måling(data):
    sleep_ms(10)
    if(data == "button"):
        p = joy2p.read()/4095
    if(data == "xakse"):
        x = joy2x.read()
    if(data == "yakse"):
        y = joy2y.read()   
    return p,x,y

