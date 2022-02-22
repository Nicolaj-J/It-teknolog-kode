import network
from esp import espnow
from machine import Pin, PWM, ADC
import time
import _thread
import servo1, servo2, servo3, servo4
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
        x = msg.decode('utf-8')
        chooseservo = x[0:2]
        value = x[2:6]
        if(chooseservo == "b1"):
            servo1.Servo1Stat.servooption = True
            servo2.Servo2Stat.servooption = True
            servo3.Servo3Stat.servooption = True
            servo4.Servo4Stat.servooption = True
            _thread.start_new_thread(servo1.Servo1, ())
            _thread.start_new_thread(servo2.Servo2, ())
            _thread.start_new_thread(servo3.Servo3, ())
            _thread.start_new_thread(servo4.Servo4, ())
        if(chooseservo == "b2"):
            servo1.Servo1Stat.servooption = False
            servo2.Servo2Stat.servooption = False
            servo3.Servo3Stat.servooption = False
            servo4.Servo4Stat.servooption = False
        if(chooseservo == "x1"):
            servo1.Servo1Stat.joystickmeasurement = value
        if(chooseservo == "y1"):
            servo1.Servo1Stat.joystickmeasurement = value
        if(chooseservo == "x2"):
            servo1.Servo1Stat.joystickmeasurement = value
        if(chooseservo == "y2"):
            servo1.Servo1Stat.joystickmeasurement = value
        x = ""
        chooseservo = ""
        value = ""
        time.sleep(0.1)

