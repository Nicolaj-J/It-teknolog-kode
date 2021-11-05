import time

ekstra_tid = 5

def t_tid(tid):
    ekstra_tid = int(tid)
    print("ekstra tid er nu", ekstra_tid)

def k_tid():
    print("k_tid begyndt")
    global ekstra_tid
    time.sleep(10)
    print("10 sekunder ovre")
    time.sleep(ekstra_tid)
    print("halvej ovre")
