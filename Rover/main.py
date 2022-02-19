import servo1, servo2, servo3, servo4
import _thread

_thread.start_new_thread(servo1.servo1, ())
_thread.start_new_thread(servo2.servo2, ())
_thread.start_new_thread(servo3.servo3, ())
_thread.start_new_thread(servo4.servo4, ())