from opcua import Client
import time
import queue
import sys

# Stego-Dictionary
dct = {
"a": "328","b": "090","c": "648","d": "977","e": "778","f": "324","g": "709","h": "351","i": "818","j": "370","k": "933","l": "810","m": "897","n": "573","o": "409","p": "548","q": "173","r": "849","s": "383","t": "169","u": "736","v": "124","w": "296","x": "715","y": "508","z": "504","A": "291","B": "661","C": "354","D": "281","E": "847","F": "823","G": "429","H": "222","I": "567","J": "111","K": "878","L": "463","M": "170","N": "844","O": "983","P": "655","Q": "598","R": "419","S": "979","T": "268","U": "928","V": "795","W": "056","X": "022","Y": "270","Z": "953","0": "596","1": "304","2": "752","3": "903","4": "315","5": "714","6": "677","7": "431","8": "342","9": "868",".": "501",",": "217"," ": "806"
}

# aufteilen der Schlüssel Ziffer für Ziffer
q = queue.Queue()
def split(string):
    length = len(string)
    for i in string:
        if i in dct:
            var = dct.get(i)
            q.put(var[0])
            q.put(var[1])
            q.put(var[2])
        else:
            var = dct.get(" ")
            q.put(var[0])
            q.put(var[1])
            q.put(var[2])

# Verbindung mit dem Server
# url = "opc.tcp://10.0.30.103:4840"
url = "opc.tcp://127.0.0.1:4840"
client = Client(url)

# Eingeben der geheimen Botschaft zur Laufzeit
string = input("Please enter your String: ")
split(string)

# Einbetten der Stego
while True:
    client.connect()
    # print("Client has connected succesfully")
    # print("Avaialbe Namespaces: ", client.get_namespace_array())    
    tempC = client.get_node("ns = 2; i = 2")
    val = tempC.get_value()[:-1]
    tmp = q.get()
    res = val + tmp
    print(res)
    tempC.set_value(res)
    if q.empty():
        break
    time.sleep(2)
    client.disconnect()
client.disconnect()  


