from opcua import Client
import time

url = "opc.tcp://127.0.0.1:4840"
client = Client(url)

client.connect()
print("Client connected")

while True:
	Temp = client.get_node("ns=2; i=2")
	Temperature = Temp.get_value()
	print(Temperature)
	time.sleep(2)
