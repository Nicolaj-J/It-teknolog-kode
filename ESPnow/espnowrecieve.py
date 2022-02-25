import network
from esp import espnow
from machine import Pin, PWM, ADC
servo1=PWM(Pin(22),freq=50)

# A WLAN interface must be active to send()/recv()
w0 = network.WLAN(network.STA_IF)
w0.active(True)

e = espnow.ESPNow()
e.init()
peer = b'@\x91Q\xabV\xb4'   # MAC address of peer's wifi interface
e.add_peer(peer)

while True:
    host, msg = e.irecv()     # Available on ESP32 and ESP8266
    if msg:             # msg == None if timeout in irecv()
        print(host, msg)
        print(type(msg))
        if msg == int:
            servo1.duty(msg)
        if msg == b'end':
            break
