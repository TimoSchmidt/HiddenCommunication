from opcua import Client
from random import randint
import time

# server address
url = "opc.tcp://127.0.0.1:4840"
client = Client(url)

client.connect()
print("Client connected")
    
try:
    while True:
        # get the server node
        temperature = client.get_node("ns = 2; i = 2")
        # set the node's value
        rand = randint(0, 40)
        temperature.set_value(rand)
        print(temperature.get_value())
    
        time.sleep(1)
finally:
    client.disconnect()
