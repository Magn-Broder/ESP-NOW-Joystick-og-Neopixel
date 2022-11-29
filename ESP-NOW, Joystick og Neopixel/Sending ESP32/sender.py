import network
import espnow

sta = network.WLAN(network.STA_IF)
sta.active(True)

e = espnow.ESPNow()
e.active(True)

peer = b'\x0c\xb8\x15\xc5\x4e\x28'
e.add_peer(peer)

e.send("Starting...")
for i in range(5):
    e.send(peer, str(i+1)+". hej")
    
    