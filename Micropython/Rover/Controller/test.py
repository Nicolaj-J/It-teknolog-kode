import tm1637
from machine import Pin
import time
tm = tm1637.TM1637(clk=Pin(2), dio=Pin(0))

# dim
tm.brightness(0)
time.sleep(1)
tm.brightness(1)
time.sleep(1)
tm.brightness(2)
time.sleep(1)
tm.brightness(3)
time.sleep(1)
tm.brightness(4)
time.sleep(1)
tm.brightness(5)
time.sleep(1)
tm.brightness(6)
# 1234
tm.write([0x06, 0x5B, 0x4F, 0x66])
time.sleep(1)
# 1.234
tm.write([0x06 | 128, 0x5B, 0x4F, 0x66])
time.sleep(1)
# 12.34
tm.write([0x06, 0x5B | 128, 0x4F, 0x66])
time.sleep(1)
# 1.2.3.4.
tm.write([0x06 | 128, 0x5B | 128, 0x4F | 128, 0x66 | 128])
time.sleep(1)
# help
tm.show('help')


time.sleep(1)
tm.write('hej')
