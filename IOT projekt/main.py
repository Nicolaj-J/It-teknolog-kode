import umqtt_robust2
from machine import Pin
import GPSfunk
from time import sleep_ms, sleep
import like
import gps
import _thread
# import settings
import puls_sensor
lib = umqtt_robust2
like.start_up()
# _thread.start_new_thread(settings.setting, ("1",))
likes = 0
while True:
    sleep_ms(500)
    besked = lib.besked
    # haandtere fejl i forbindelsen og hvor ofte den skal forbinde igen
    if lib.c.is_conn_issue():
        while lib.c.is_conn_issue():
            # hvis der forbindes returnere is_conn_issue metoden ingen fejlmeddelse
            lib.c.reconnect()
        else:
            lib.c.resubscribe()
    try:
        # Det er primært herinde at i skal tilfoeje kode
        if besked == "like":
            like.likes(70, 204, 235)
            likes = likes + 1
            like.likes_count(likes)
            lib.besked = ""
        if besked == "like reset":
            likes = 0
            print(likes)
            lib.besked = ""
        if besked == "gps start":
            gps_status = 1
            _thread.start_new_thread(gps.gps_loc, ())
            lib.besked = ""
        if besked == "hastighed start":
            _thread.start_new_thread(gps.hastighed, ())
            lib.besked = ""
        if besked == "start puls":
            _thread.start_new_thread(puls_sensor.puls_funktion, ())
            _thread.start_new_thread(puls_sensor.timer, ())
            lib.besked = ""
    except KeyboardInterrupt:
        print('Ctrl-C pressed...exiting')
        lib.client.disconnect()
        lib.sys.exit()
    except OSError as e:
        print('Failed to read sensor.')
    lib.c.check_msg() # needed when publish(qos=1), ping(), subscribe()
    lib.c.send_queue()  # needed when using the caching capabilities for unsent messages
lib.c.disconnect()
