import umqtt_robust2
from machine import Pin
import dht
import time
import like
import random
import _thread
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
    def publishbesked():
        global besked_p
        lib.c.publish(tpic=lib.mqtt_pub_feedname, msg= besked_p)
        lib.besked = ""
        besked_p = ""
    try:
        if besked == "hej bot":
            besked_p = "Hej Master"
            publishbesked()
        if besked == "joke":
            besked_p = jokes.joke_funktion(random.choice(joke_list))
            publishbesked()
        def like_counter()
            global besked
            if besked == "like":
                like.like()
            time.sleep(0,2)
        def puls_timer()
        def kmt_timer()
        def gps_timer()
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
