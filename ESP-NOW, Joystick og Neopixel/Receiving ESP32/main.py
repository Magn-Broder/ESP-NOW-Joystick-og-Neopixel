import network
import espnow
from neopixel import NeoPixel
from machine import Pin
from time import sleep

n = 12
p = 17
np = NeoPixel(Pin(p),n)

def np_off():
    for i in range(n):
        np[i] = (0, 0, 0)
        np.write()

def set_np(pixel, r=0, g=0, b=0):
    np[pixel] = (r, g, b)
    np.write()
        
sta = network.WLAN(network.STA_IF)
sta.active(True)

e = espnow.ESPNow()
e.active(True)

peer = b'\xbb\xbb\xbb\xbb\xbb\xbb'
e.add_peer(peer)

while True:
    host,msg = e.recv()
    msg = msg.decode('utf-8')
    j_data = msg.split(",")
    
    if msg:
        print(j_data)
        
    if int(j_data[0]) == 0:
        set_np(3, 25)
    elif int(j_data[0]) == 4095:
        set_np(9, 25)
    elif int(j_data[1]) == 0:
        set_np(0, 25)
    elif int(j_data[1]) == 4095:
        set_np(6, 25)
    else:
        np_off()
    
