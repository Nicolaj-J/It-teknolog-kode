import _thread
import time
def test():
    for x in range (5):
        print("hej")
        time.sleep(1)
    _thread.exit()


def timer():
    while True:
        _thread.start_new_thread(test, ())
        time.sleep(15)
        print("ny tråd er startet")

_thread.start_new_thread(timer, ())
