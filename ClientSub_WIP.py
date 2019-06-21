from opcua import Client
import time

url = "opc.tcp://10.0.30.103:4840"
client = Client(url)

class SubHandler(object):

    def datachange_notification(self, node, val, data):
        print("New data change event", node, val)


while True:
    client.connect()
    Temp = client.get_node("ns=2; i=2")
    Temperature = Temp.get_value()

    handler = SubHandler()
    sub = client.create_subscription(2000, handler)
    handler = sub.subscribe_data_change(Temp)
    
    # print(Temperature)
    # time.sleep(2)
    client.disconnect()
