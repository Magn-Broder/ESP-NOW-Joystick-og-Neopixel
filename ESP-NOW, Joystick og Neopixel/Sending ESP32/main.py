from machine import ADC, Pin
from time import sleep
import network
import espnow

x = Pin(35)
y = Pin(34)
btn = Pin(4)
x_joy = ADC(x)
y_joy = ADC(y)
x_joy.atten(ADC.ATTN_11DB)
x_joy.width(ADC.WIDTH_12BIT)
y_joy.atten(ADC.ATTN_11DB)
y_joy.width(ADC.WIDTH_12BIT)

sta = network.WLAN(network.STA_IF)
sta.active(True)

e = espnow.ESPNow()
e.active(True)

peer = b'\xbb\xbb\xbb\xbb\xbb\xbb'
e.add_peer(peer)

e.send("Starting...")

while True:
    x_val_raw = x_joy.read()
    y_val_raw = y_joy.read()
    sendvalue = f'{x_val_raw},{y_val_raw},{str(btn.value())}'
    print(f"x {x_val_raw} y {y_val_raw} btn {btn.value()}")
    e.send(peer, sendvalue)
    sleep(0.1)

