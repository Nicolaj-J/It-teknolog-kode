import umqtt_robust2
from machine import Pin
import GPSfunk
from time import sleep_ms, sleep
import like
import gps
import _thread
import puls_sensor
lib = umqtt_robust2
like.start_up() #Devicet køre start funktionen for tæller og led ring
lib.c.publish(topic=lib.mqtt_pub_feedname, msg="device connected") #Devicet skriver ud når den er har forbundet op til adafruit og alle startups fungere
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
        """Her sortere vi i den data der bliver sendt til devicet.
           Vi fordeler ud på funktioner og nogle bliver lavet til tråde """
        if besked == "test":
            lib.c.publish(topic=lib.mqtt_pub_feedname, msg="Forbundet")
            lib.besked = ""
        if besked == "like":
            like.likes(70, 204, 235)
            likes = likes + 1
            like.likes_count(likes)
            lib.besked = ""
        if besked == "like reset":
            likes = 0
            like.likes_count(likes)
            lib.besked = ""
        if lib.gpsbesked == "gps start":
            _thread.start_new_thread(gps.gps_status, ("start",))
            lib.besked = ""
        if lib.gpsbesked == "gps stop":
            _thread.start_new_thread(gps.gps_status, ("stop",))
            lib.besked = ""
        if lib.kmtbesked == "hastighed start":
            gps.hastighed_status("start")
            lib.besked = ""
        if lib.kmtbesked == "hastighed stop":
            gps.hastighed_status("stop")
            lib.besked = ""
        if lib.pulsbesked == "puls start":
            puls_sensor.puls_styring("start")
            lib.besked = ""
        if lib.pulsbesked == "puls stop":
            puls_sensor.puls_styring("stop")
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
