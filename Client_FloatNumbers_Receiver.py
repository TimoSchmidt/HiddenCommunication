from opcua import Client
import time

dct = {
    "99": "a", "41": "b", "68": "c", "93": "d", "23": "e", "71": "f", 
    "01": "g", "03": "h", "13": "i", "37": "j", "20": "k", "67": "l", 
    "58": "m", "24": "n", "83": "o", "97": "p", "10": "q", "80": "r", 
    "19": "s", "20": "t", "21": "u", "22": "v", "23": "w", "24": "x", 
    "25": "y", "26": "z"    
    }

dct2 = {
    "00": "h", "42": "e", "87": "l", "66": "o"
}
url = "opc.tcp://10.0.21.175:4840"
client = Client(url)

client.connect()
print("Client has connected succesfully")
#print("Avaialbe Namespaces: ", client.get_namespace_array())

val = "b"
while True:
    recTempC = client.get_node("ns = 2; i = 2")
    val = val + recTempC.get_value()[-1:]
    print("test: ", val)
    if(val in dct2):
        print(dct2.get(val))
        val = "b"
    else:
        val = val[-1:]
    time.sleep(3)
client.disconnect()
        

