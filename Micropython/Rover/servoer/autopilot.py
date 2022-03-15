from hcsr04 import HCSR04
from time import sleep, sleep_ms
from machine import Pin, ADC, PWM
import _thread
import motorstyring
sensor_højre = HCSR04(trigger_pin=18, echo_pin=5, echo_timeout_us=10000)
sensor_venstre = HCSR04(trigger_pin=33, echo_pin=25, echo_timeout_us=10000)
class Autopilotstat:
    Autopilotoption = False
    SensorHmåling = 0
    SensoreVmåling = 0
#     listehøj = []
#     listeven = []
    tid = 150
    speed = 400
    avgdifint = 5

# def Autopilotmåling():
#     while(Autopilotstat.Autopilotoption == True):
#         distance_høj = sensor_højre.distance_cm()
#         distance_ven = sensor_venstre.distance_cm()
#         print("høj: ", distance_høj, "ven: ", distance_ven)
#         Autopilotstat.listehøj.append(distance_høj)
#        Autopilotstat.listeven.append(distance_ven)
#         sleep_ms(Autopilotstat.tid)

def autopilot_udregning():
    while(True):
        check = Autopilotstat.Autopilotoption
        if(check == False):
            _thread.exit()
            break
        distance_høj = sensor_højre.distance_cm()
        distance_ven = sensor_venstre.distance_cm()
        motorstyring.Motorstat.hdirection = 0
        motorstyring.Motorstat.vdirection = 0
        sleep_ms(int(Autopilotstat.tid))
        avg = distance_ven - distance_høj
        print("avg: ", avg)
        # print("avgh: ", avgh, "avgv: ", avgv, "avg: ", avg)
        if distance_ven < 1 or distance_høj < 1:
            pass
        elif(distance_høj < 10):
            motorstyring.Motorstat.hspeed = Autopilotstat.speed
            motorstyring.Motorstat.vspeed = 200
        elif(distance_ven < 10):
            motorstyring.Motorstat.vspeed = Autopilotstat.speed
            motorstyring.Motorstat.hspeed = 200

        elif(avg > 1):
            avgdif = abs(avg) * 50 #(Autopilotstat.speed/Autopilotstat.avgdifint)
            if(avgdif > 250):
                motorstyring.Motorstat.hspeed = 200
            else:
                motorstyring.Motorstat.hspeed = Autopilotstat.speed - int(avgdif)
            motorstyring.Motorstat.vspeed = Autopilotstat.speed

        elif(avg < 1):
            avgdif = abs(avg) * 50 #(Autopilotstat.speed/Autopilotstat.avgdifint)
            motorstyring.Motorstat.hspeed = Autopilotstat.speed
            if(avgdif > 250):
                motorstyring.Motorstat.vspeed = 200
            else:
                motorstyring.Motorstat.vspeed = Autopilotstat.speed - int(avgdif)
        else:
            motorstyring.Motorstat.hspeed = Autopilotstat.speed
            motorstyring.Motorstat.vspeed = Autopilotstat.speed
#         print("avgdif: ", avgdif)
#         print("hspeed: ", motorstyring.Motorstat.hspeed ,"vspeed: ", motorstyring.Motorstat.vspeed)
#     _thread.exit()
