from machine import UART
from micropyGPS import MicropyGPS
import time
def main():
    print("gps main køre")
    uart = UART(2, baudrate=9600, bits=8, parity=None, stop=1, timeout=5000, rxbuf=1024)
    gps = MicropyGPS()

    print("gps main while kører")
    buf = uart.readline()
    while True:
        time.sleep(10)
        for char in buf:
            gps.update(chr(char)) # Note the conversion to to chr, UART outputs ints normally
                #print('UTC Timestamp:', gps.timestamp)
                #print('Date:', gps.date_string('longs'))
                #print('Satellites:', gps.satellites_in_use)
                #print('Altitude:', gps.altitude)
                #print('Latitude:', gps.latitude_string())
                #print('Longitude:', gps.longitude_string())
                #print('Horizontal Dilution of Precision:', gps.hdop)
        print("gps main ude af for loopet")
        formattedLat = gps.latitude_string()
        formattedLat = formattedLat[:-3]
        formattedLon = gps.longitude_string()
        formattedLon = formattedLon[:-3]
        formattedAlt = str(gps.altitude)
        formattedSpd = gps.speed_string()
        formattedSpd = formattedSpd[:-5]
        print("gps main efter formattering")

        gps_ada = formattedSpd+","+formattedLat+","+formattedLon+","+formattedAlt
        print("gps main efter sammensætning af streng")
                    # def startGPSthread():
                    # _thread.start_new_thread(main, ())
        print(gps_ada)

        if formattedLat != "0.0":
            print("gps main inde i if")
            print("gps_ada: ",gps_ada)
            return gps_ada

if __name__ == "__main__":
    print('...running main, GPS testing')
    main()
