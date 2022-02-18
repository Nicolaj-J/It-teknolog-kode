import network
from esp import espnow

# A WLAN interface must be active to send()/recv()
print(-3)
w0 = network.WLAN(network.STA_IF)  # Or network.AP_IF
print(-2)
w0.active(True)
print(-1)
e = espnow.ESPNow()
print(0)
e.init()
print("1")
peer = b'08:3a:f2:ac:34:c4'   # MAC address of peer's wifi interface
print("2")
e.get_peer(b'08:3a:f2:ac:34:c4')
print(4)
e.add_peer(peer)
print("3")
e.send("Starting...")       # Send to all peers
print("4")
for i in range(100):
    print(i)
    e.send(peer, str(i)*20, True)
    e.send(b'end')