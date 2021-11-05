def helpc():
    lib.c.publish(tpic=lib.mqtt_pub_feedname, msg= "start/stop gps")
    lib.c.publish(tpic=lib.mqtt_pub_feedname, msg= "start/stop like")
    lib.c.publish(tpic=lib.mqtt_pub_feedname, msg= "start/stop puls")
    lib.c.publish(tpic=lib.mqtt_pub_feedname, msg= "start/stop kmt")
    lib.c.publish(tpic=lib.mqtt_pub_feedname, msg= "puls tid")
    lib.c.publish(tpic=lib.mqtt_pub_feedname, msg= "gps tid")
    lib.c.publish(tpic=lib.mqtt_pub_feedname, msg= "kmt tid")
    lib.c.publish(tpic=lib.mqtt_pub_feedname, msg= )
    lib.besked = ""
