import time
import _thread
import random
sveden = 0
fejl_sved = 0
fejl_andet = 0
def sved():
    while True:
        sveden = 0.81 * random.randint(0,4095)
        post(sveden)
        time.sleep(2)

def post(sved):
    n = 0
    while True:
       time.sleep(2)
       print(sved)
       if sved >= 500:
           n = n + 1
           print("n er nu :", n)
           if n == 10:
                print("Sved værdig på 10")
                n = 0
                print("n er 0")
       else:
           n = 0
           print("n er 0")

_thread.start_new_thread(sved, ())


