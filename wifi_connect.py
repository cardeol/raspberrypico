import network
import time
import sys

if not ('./frozen' in sys.path):
    # upip.install("micropython-umqtt.simple")
    sys.path.append('/.frozen')

from umqtt.simple import MQTTClient

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("VMFFEC27A","aWvykmfyzam2")
 
# Wait for connect or fail
wait = 10
while wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    wait -= 1
    print('waiting for connection...')
    time.sleep(1)
 
# Handle connection errorin
if wlan.status() != 3:
    raise RuntimeError('wifi connection failed')
else:
    print('connected')
    print('IP: ', wlan.ifconfig())
    

def connectMQTT():
    client = MQTTClient(client_id=b"rp20.cmooo.com",
        server=b"broker.hivemq.com",
        port=1883,
        keepalive=7200,
        ssl=False,
    )

    client.connect()
    return client
    
    
client = connectMQTT()

    
