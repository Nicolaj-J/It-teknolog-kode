import umqtt_robust2
from machine import Pin
import GPSfunk
from time import sleep_ms, sleep
import like
import gps
lib = umqtt_robust2
like.start_up()
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
        if besked == "hej":
            lib.c.publish(topic=lib.mqtt_pub_feedname, msg="Hej Master")
            lib.besked = ""
        if besked == "like":
            like.likes(255,0,0)
            likes = likes + 1
            like.likes_count(likes)
            lib.besked = ""
        if besked == "like reset":
            likes = 0
            print(likes)
            lib.besked = ""
        if besked == "test":
            lib.c.publish(topic=lib.mqtt_gps_feedname, msg="poster på gps")
            lib.besked = ""
        if besked == "gps":
            print("gps")
            gps.gps_loc()
            print("gps1")
            gps.hastighed()
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
