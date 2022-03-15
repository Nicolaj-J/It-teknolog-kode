import network
from esp import espnow
from machine import Pin, PWM, ADC
buzzer = Pin(12, Pin.OUT, value=0)

# A WLAN interface must be active to send()/recv()
w0 = network.WLAN(network.STA_IF)
w0.active(True)

e = espnow.ESPNow()
e.init()
peer = b'\x08:\xf2\xab^\xdc'   # MAC address of peer's wifi interface
e.add_peer(peer)

while True:
    host, msg = e.irecv()     # Available on ESP32 and ESP8266
    if msg:             # msg == None if timeout in irecv()
        message = data.encode('utf-8')
        print(host, message)
        if(message == "buz"):
            buzzer.value(1)
        elif(message == "stop"):
            buzzer.value(0)
