from opcua import Client
import time

url = "opc.tcp://127.0.0.1:4840"
client = Client(url)

client.connect()
print("Client has connected successfully")

root = client.get_root_node()
print("Root node is: ", root)
objects = client.get_objects_node()
print("Objects node is: ", objects)

start_time = time.time()
while True:
    elapsed_time = time.time() - start_time
    if elapsed_time > 15:
        print("TIME UP")
        Temp = client.get_node("ns=2; i=2")
        Temp.set_value(10000)
        print("Client send Message")
        elapsed_time =0
        start_time = time.time()
    print (' seconds until send',elapsed_time)
    time.sleep(1)
