import umqtt_robust2
from machine import Pin
import dht
import time
import like
import random
import _thread
import like
import puls
import gps
import helpc
lib = umqtt_robust2
sensor = dht.DHT11(Pin(14))
besked_p = ""

while True:
    time.sleep(5)
    besked = lib.besked
    if lib.c.is_conn_issue():
        while lib.c.is_conn_issue():
            lib.c.reconnect()
        else:
            lib.c.resubscribe()
    try:
        if besked == "help":
            helpc.helpc()
        if besked == "tillægs tid" or "tillæg tid")
            print("Hvor meget tillægs tid er der? skriv i sekunder"
            kamp_tid.t_tid(input)
        if besked == "kamp start":
            kamp_tid.k_tid()
        def like_counter()
            global besked
            if besked == "like":
                like.like()
            time.sleep(0,2)
        def puls_timer()
            status = 0
            tid = 1
            while True:
            time.sleep(tid)
            if besked == "stop puls":
                status = 0
            elif besked == "start puls":
                status = 1
            if status == 0:
                pass
            elif status == 1:
                puls.puls()
        def kmt_timer()
            status = 0
            tid = 1
            while True:
            time.sleep(tid)
            if besked == "stop kmt":
                status = 0
            elif besked == "start kmt":
                status = 1
            if status == 0:
                pass
            elif status == 1:
                gps.kmt()
        def gps_timer()
            status = 0
            tid = 1
            while True:
            time.sleep(tid)
            if besked == "stop gps":
                status = 0
            elif besked == "start gps":
                status = 1
            if status == 0:
                pass
            elif status == 1:
                gps.gps()
    except KeyboardInterrupt:
        print('Ctrl-C pressed...exiting')
        lib.client.disconnect()
        lib.sys.exit()
    except OSError as e:
        print('Failed to read sensor.')
    lib.c.check_msg()
    lib.c.send_queue()
    _thread.start_new_thread(like_counter, ())
    _thread.start_new_thread(puls_timer, ())
    _thread.start_new_thread(kmt_timer, ())
    _thread.start_new_thread(gps_timer, ())

lib.c.disconnect()
