import network
from esp import espnow
from machine import Pin, PWM, ADC
import time
import _thread
import servo1, servo2, servo3, servo4
import joystickconversion
import motorstyring
import autopilot
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
        mode = x[0:1]
        chooseservo = x[1:3]
        value = x[3:7]

        if(mode == "s"):
            if(servo1.Servo1Stat.servooption != True):
                joystickconversion.Joystickconstat.joystickconversionoption = False
                autopilot.Autopilotstat.Autopilotoption = False
                servo1.Servo1Stat.servooption = True
                servo2.Servo2Stat.servooption = True
                servo3.Servo3Stat.servooption = True
                servo4.Servo4Stat.servooption = True
                time.sleep(0.5)
                try:
                    _thread.start_new_thread(servo1.Servo1, ())
                except:
                    print("Servo1 kunne ikke starte")
                try:
                    _thread.start_new_thread(servo2.Servo2, ())
                except:
                    print("Servo2 kunne ikke starte")
                try:
                    _thread.start_new_thread(servo3.Servo3, ())
                except:
                    print("Servo3 kunne ikke starte")
                try:
                    _thread.start_new_thread(servo4.Servo4, ())
                except:
                    print("Servo4 kunne ikke starte")
            if(chooseservo == "x1" and servo1.Servo1Stat.servooption == True):
                servo1.Servo1Stat.joystickmeasurement = int(value)
            if(chooseservo == "y1" and servo1.Servo1Stat.servooption == True):
                servo2.Servo2Stat.joystickmeasurement = int(value)
            if(chooseservo == "x2" and servo1.Servo1Stat.servooption == True):
                servo3.Servo3Stat.joystickmeasurement = int(value)
            if(chooseservo == "y2" and servo1.Servo1Stat.servooption == True):
                servo4.Servo4Stat.joystickmeasurement = int(value)
        if(mode == "a"):
            if(autopilot.Autopilotstat.Autopilotoption == False):
                joystickconversion.Joystickconstat.joystickconversionoption = False
                servo1.Servo1Stat.servooption = False
                servo2.Servo2Stat.servooption = False
                servo3.Servo3Stat.servooption = False
                servo4.Servo4Stat.servooption = False
                autopilot.Autopilotstat.Autopilotoption = True
                # _thread.start_new_thread(autopilot.Autopilotmåling,())
                try:
                    _thread.start_new_thread(autopilot.autopilot_udregning,())
                except:
                    print("kunne ikke starte autopilot")
        if(mode == "m"):
            if(joystickconversion.Joystickconstat.joystickconversionoption == False):
                servo1.Servo1Stat.servooption = False
                servo2.Servo2Stat.servooption = False
                servo3.Servo3Stat.servooption = False
                servo4.Servo4Stat.servooption = False
                autopilot.Autopilotstat.Autopilotoption = False
                joystickconversion.Joystickconstat.joystickconversionoption = True
                motorstyring.Motorstat.motoroption = True
                try:
                    _thread.start_new_thread(joystickconversion.Conversion, ())
                except:
                    print("kunne ikke starte manuel joystick")
                try:
                    _thread.start_new_thread(motorstyring.h_motorer, ())
                except:
                    print("kunne ikke starte højre motor set")
                try:
                    _thread.start_new_thread(motorstyring.v_motorer, ())
                except:
                    print("kunne starte venstre motor set")
            if(chooseservo == "x1" and joystickconversion.Joystickconstat.joystickconversionoption == True):
                joystickconversion.Joystickconstat.joystickxreading = int(value)

            if(chooseservo == "y1" and joystickconversion.Joystickconstat.joystickconversionoption == True):
                joystickconversion.Joystickconstat.joystickyreading = int(value)

        x = ""
        chooseservo = ""
        value = ""

