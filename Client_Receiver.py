from opcua import Client
import time

dct = {
    "1": "a", "2": "b", "3": "c", "4": "d", "5": "e", "6": "f", 
    "7": "g", "8": "h", "9": "i", "10": "j", "11": "k", "12": "l", 
    "13": "m", "14": "n", "15": "o", "16": "p", "17": "q", "18": "r", 
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
        

