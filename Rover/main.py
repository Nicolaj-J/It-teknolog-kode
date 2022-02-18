import servo1, servo2, servo3, servo4
import servostyring
import _thread

while(True):
    x = input()
    if(x == "start"):
        servostyring.servo1control("start")
    elif(x == "stop"):
        servostyring.servo1control("stop")
