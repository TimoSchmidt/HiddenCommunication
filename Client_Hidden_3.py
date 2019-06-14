from opcua import Client
from random import randint 
import time
import queue
from math import trunc
import sys

url = "opc.tcp://127.0.0.1:4840"
client = Client(url)

client.connect()
print("Client has connected succesfully")
print("Avaialbe Namespaces: ", client.get_namespace_array())

dct = {
"a": "328","b": "090","c": "648","d": "977","e": "778","f": "324","g": "709","h": "351","i": "818","j": "370","k": "933","l": "810","m": "897","n": "573","o": "409","p": "548","q": "173","r": "849","s": "383","t": "169","u": "736","v": "124","w": "296","x": "715","y": "508","z": "504","A": "291","B": "661","C": "354","D": "281","E": "847","F": "823","G": "429","H": "222","I": "567","J": "111","K": "878","L": "463","M": "170","N": "844","O": "983","P": "655","Q": "598","R": "419","S": "979","T": "268","U": "928","V": "795","W": "056","X": "022","Y": "270","Z": "953","0": "596","1": "304","2": "752","3": "903","4": "315","5": "714","6": "677","7": "431","8": "342","9": "868",".": "501",",": "217"," ": "806"
}

queueie = queue.Queue()

string = input("Please enter your String: ") # sys.argv[1]
#string = string + " "
#print(len(string))
def split(string):
    length = len(string)
    for i in string:
        #cha = string[i]
        if i in dct:
            var = dct.get(i)
            queueie.put(var[0])
            queueie.put(var[1])
            queueie.put(var[2])
        else:
            var = dct.get(" ")
            queueie.put(var[0])
            queueie.put(var[1])
            queueie.put(var[2])

split(string)

#tmp = client.get_node("ns = 2; i = 2")
#tmp.set_value("24.871")
#print(list(queueie.queue))

while True:
    client.connect()
    #for i in range(0, 1):
    tempC = client.get_node("ns = 2; i = 2")
    val = tempC.get_value()[:-1]
    tmp = queueie.get()
    res = val + tmp
    print(res)
    queueie.put(tmp)
    tempC.set_value(res)
    time.sleep(2)
    client.disconnect()

   
    


