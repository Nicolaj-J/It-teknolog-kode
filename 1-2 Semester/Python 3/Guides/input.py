import time

status = 0
tid = 1
while True:
    time.sleep(int(tid))
    print("køre i loopet")
    if besked == "stop puls":
        print("stopper puls")
        status = 0
    elif besked == "start puls":
        print("start puls")
        status = 1
    if besked == "puls tid":
        print("Skriv hvor tit puls målingen skal ske")
        tid = input()
        print("Måler nu puls med ", tid, " sekunder mellemrum")
        besked = ""
        pass
    if status == 0:
        ("puls er stoppet")
        pass
    elif status == 1:
        print("funktionen køre")
print("ude af while loopet")
