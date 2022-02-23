import network
from esp import espnow
# A WLAN interface must be active to send()/recv()
w0 = network.WLAN(network.STA_IF)  # Or network.AP_IF
w0.active(True)
e = espnow.ESPNow()
e.init()
peer = b'\x08:\xf2\xac4\xc4'   # MAC address of peer's wifi interface
e.add_peer(peer)

def SendData(data):

    print(data)
    x = data.encode('utf-8')
    print(x)
    e.send(x)
