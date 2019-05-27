from opcua import Client
import time

dct = {
    "1": "a", "2": "b", "3": "c", "4": "d", "5": "e", "6": "f", 
    "7": "g", "8": "h", "9": "i", "10": "j", "11": "k", "12": "l", 
    "13": "m", "14": "n", "15": "o", "16": "p", "17": "q", "18": "r", 
    "19": "s", "20": "t", "21": "u", "22": "v", "23": "w", "24": "x", 
    "25": "y", "26": "z"    
    }

url = "opc.tcp://127.0.0.1:4840"
client = Client(url)

client.connect()
print("Client has connected succesfully")
#print("Avaialbe Namespaces: ", client.get_namespace_array())

try:
    while True:
        recTempC = client.get_node("ns = 2; i = 2")
        val = recTempC.get_value()
        truncTxt = val[5:7]
        if(truncTxt):
            print(dct.get(truncTxt))
        time.sleep(0.5)
finally:
    client.disconnect()
