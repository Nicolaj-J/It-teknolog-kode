import network
from esp import espnow

# A WLAN interface must be active to send()/recv()
w0 = network.WLAN(network.STA_IF)  # Or network.AP_IF
w0.active(True)

mac = w0.config('mac')
print (mac)
