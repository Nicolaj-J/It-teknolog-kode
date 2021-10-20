# Importere library til at forbinde til adafruit.io
import umqtt_robust2
from machine import Pin
import dht
from time import sleep_ms, sleep
import random
lib = umqtt_robust2
led = Pin(27, Pin.OUT, value=0)
sensor = dht.DHT11(Pin(14))
jokenr = 0

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
        if besked == "hej Bot":
            lib.c.publish(topic=lib.mqtt_pub_feedname, msg="Hej Master")
            lib.besked = ""
        if besked == "klima":
            try:
                sensor.measure()
                temp = sensor.temperature()
                hum = sensor.humidity()
                tempf =  temp * (9/5) + 32.0
                lib.c.publish(topic=lib.mqtt_pub_feedname, msg='Temperatur: %3.1f C' %temp)
                lib.c.publish(topic=lib.mqtt_pub_feedname, msg='Temperatur: %3.1f F' %tempf)
                lib.c.publish(topic=lib.mqtt_pub_feedname, msg='Luftfugtighed: %3.1f procent' %hum)
                lib.besked = ""
            except OSError as e:
                lib.c.publish(topic=lib.mqtt_pub_feedname, msg="Failed to read sensor.")
                lib.besked = ""
        if besked == "temp":
            lib.c.publish(topic=lib.mqtt_pub_feedname, msg='Temperatur: %3.1f C' %temp)
            lib.c.publish(topic=lib.mqtt_pub_feedname, msg='Temperatur: %3.1f F' %tempf)
            lib.besked = ""
            if temp > 30:
                for x in range(4):
                    lib.c.publish(topic=lib.mqtt_pub_feedname, msg='Det for varmt')
                    lib.besked = ""
            if temp < 20:
                for x in range(4):
                    lib.c.publish(topic=lib.mqtt_pub_feedname, msg='Det for koldt')
                    lib.besked = ""
            lib.besked = ""
        if besked == "tænd lys":
            led.value(True)
            lib.besked = ""
        if besked == "sluk lys":
            led.value(False)
            lib.besked = ""
        if besked == "lys":
            led.value(not led.value())
            lib.besked = ""
        if besked == "fortæl en joke":
            lib.c.publish(topic=lib.mqtt_pub_feedname, msg='Hvad kalder man en magisk hund? Labracadabrador')
            lib.besked = ""
        if besked == "fortæl en joke mere":
            lib.c.publish(topic=lib.mqtt_pub_feedname, msg='Jeg overvejer at gifte mig med en tysker. Er det over grænsen?')
            lib.besked = ""
        if besked == "fortæl en tilfældig joke":
            jokenr = random.randint(0, 8)
            def joke_funktion(*joke):
                    lib.c.publish(topic=lib.mqtt_pub_feedname, msg= joke[jokenr])
                    #print("Her er en joke: " + joke[jokenr])
                    sleep(5)
            joke_funktion("En røver kommer ind i butikken og stjæler et TV. blondinen løber efter ham og råber, Vent, du har glemt fjernbetjeningen!"
            ,"Hvor langt kan en negere løbe i gennemsnittet? /nTil kæden strammer",
            "Hvad kalder man en indbagt haj /nhaj med dej",
            "Hvad laver edderkoppen når den keder sig?  Den går på nettet",
            "Ja, du har ringet til selvmords linjen, bliv lige hængende",
            "Hvis mænd kan få deres sexbehov dækket med et pornoblad, kan de så også få stillet deres sult med en kogebog?",
            "Hvad står der bag i bedemandens bil?  /nBare overhal mig, jeg kommer og henter dig senere.",
            "Hvad kalder man en kvindelig gartner?  /nEn plantesæk!",
            "Hvorfor blev dykkeren fyret? /nHan var alt for overfladisk!")
            lib.besked = ""
    # Stopper programmet når der trykkes Ctrl + c
    except KeyboardInterrupt:
        print('Ctrl-C pressed...exiting')
        lib.client.disconnect()
        lib.sys.exit()
    except OSError as e:
        print('Failed to read sensor.')
    lib.c.check_msg() # needed when publish(qos=1), ping(), subscribe()
    lib.c.send_queue()  # needed when using the caching capabilities for unsent messages
lib.c.disconnect()


