from machine import Pin
import neopixel
import time
import tm1637
tm = tm1637.TM1637(clk=Pin(2), dio=Pin(0))
'''neopixel bliver importeret til at styre vores led ring
   tm1637 bliver importeret til at styre tælleren'''

n = 12
p = 15
np = neopixel.NeoPixel(Pin(p), n)

def likes(r, g, b):#Styre led ringen. Den får en farve når main kalder funktionen.
    for i in range(n): #dette forloop tænder led ringen
        np[i] = (r, g, b)
    np.write()
    time.sleep(0.2)
    for i in range(n): #dette slukker led ringen
        np[i] = (0,0,0)
        np.write()

def likes_count(likes): #styre tæller og skriver de tal ud som den får med når man kalder funktionen.
    tm.brightness(6) #Sætter lys styrken
    tm.number(int(likes)) #Kalder funktionen i tm1637 bibloteket som skriver tallet ud på tælleren
    print(likes)

def start_up(): #styre start up fasen på led ring og tæller
    for i in range(n): #Led ringen starter op med en led lys lysende grøn derfor slukker vi alle
        np[i] = (0,0,0)
        np.write()
    tm.number(0) #samt starter tæller med lys i tilfældige steder. Så her sørger vi for at der står 0




