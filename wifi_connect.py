import network
import time
import sys

if not ('./frozen' in sys.path):
    # upip.install("micropython-umqtt.simple")
    sys.path.append('/.frozen')

from umqtt.simple import MQTTClient
import json
import binascii


SIMPLE_KEY = 'be8c8e648c424c0e'
TOPIC = "/c13d0650-ca48-43db-95a1-na-1"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("VMFFEC27A","aWvykmfyzam2")

client = MQTTClient(client_id=b"rp20.123456.car1234",
    server=b"broker.hivemq.com",
    port=1883,
    keepalive=7200,
    ssl=False
)
client.connect()

connected = False

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
    connected = True
    

def encode_to_base64(string):
    string_bytes = string.encode('utf-8')
    base64_bytes = binascii.b2a_base64(string_bytes)
    return base64_bytes.decode('utf-8')


def rot13(s):
    d = {}
    for c in (65, 97):
        for i in range(26):
            d[chr(i+c)] = chr((i+13) % 26 + c)
    return "".join([d.get(c, c) for c in s])

def encrypt(obj):
    key = SIMPLE_KEY
    text = json.dumps({'d': obj})
    result = key + rot13(encode_to_base64(text))
    print(result)
    return result

def publish(message):
    global connected
    global client
    if not connected:
        raise RuntimeError('mqtt not connected')
    action = { 'action': message }
    print("sending message",message)
    client.publish(TOPIC, encrypt(action))
   

    
