import time
n_navn = ["1","2"]
n_kode = ["1","2"]
n = 0
def forbind():
    #wifi = network.WLAN(network.STA_IF)
    #wifi.active(True)
    global n
    while True:
        time.sleep(1)
        print("Øverst i while")
        try:
            print(n_navn[n], n_kode[n])
            n = n + 1
            #wifi.connect(n_navn, WIFI_PASSWORD)
        except:
            print("kan ikke forbinde")
            break
forbind()
