import time
from threading import Thread
class SimpleThread(Thread):
    def __init__(self, name: str, delay: int):
        super().__init__()
        self.name = name
        self.delay = delay
    def run(self):
        for loop in range(5):
            print("Name: %d %s" % (loop, self.name))
            time.sleep(self.delay)

t1 = SimpleThread('Bo',2)
t2 = SimpleThread('Bob', 4)
t3 = SimpleThread('børge', 10)

t1.start()
t2.start()
t3.start()
