from opcua import Client
import time

# Stego-Dictionary
dct = {
"328": "a","090": "b","648": "c","977": "d","778": "e","324": "f","709": "g","351": "h","818": "i","370": "j","933": "k","810": "l","897": "m","573": "n","409": "o","548": "p","173": "q","849": "r","383": "s","169": "t","736": "u","124": "v","296": "w","715": "x","508": "y","504": "z","291": "A","661": "B","354": "C","281": "D","847": "E","823": "F","429": "G","222": "H","567": "I","111": "J","878": "K","463": "L","170": "M","844": "N","983": "O","655": "P","598": "Q","419": "R","979": "S","268": "T","928": "U","795": "V","056": "W","022": "X","270": "Y","953": "Z","596": "0","304": "1","752": "2","903": "3","315": "4","714": "5","677": "6","431": "7","342": "8","868": "9","501": ".","217": ",","806": " "
}

# Verbindung mit dem Server
# url = "opc.tcp://10.0.30.103:4840"
url = "opc.tcp://127.0.0.1:4840"
client = Client(url)

# Funktion zum Extrahieren der Stego
counter = 0
def extract(val):
    global counter
    res = ""
    if counter <= 2:
        recvMes = client.get_node("ns = 2; i = 2")
        val = val + recvMes.get_value()[-1:]
        counter = counter + 1
        print("Cipher: ", val)
    if counter == 3:
        if val in dct:
            res = dct.get(val)
            print("Message contains: " + res)
            val = ""
            counter = 0
        else:
            val = val[-2:]
            counter = counter - 1
    return val, res

start = "aaa" 
stop = "zzz"
stopSigRecv = False
cmpSignal = ""

val = ""

while True:
    client.connect()
    # print("Client has connected succesfully") 
    # print("Avaialbe Namespaces: ", client.get_namespace_array())
    
    # Startsignal empfangen
    print("Receiving Startsignal...")    
    val, tmp = extract(val)
    cmpSignal = cmpSignal + tmp
    if len(cmpSignal) == 3:
        if cmpSignal != start:
            cmpSignal = cmpSignal[1:]
        else:
            # Botschaft empfangen        
            print("Startsignal received.\n\nReceiving message...")
            time.sleep(2)
            cmpSignal = val = ""
            while True:
                val, tmp = extract(val)
                cmpSignal = cmpSignal + tmp
                if len(cmpSignal) == 3:
                    if cmpSignal != stop:
                        cmpSignal = cmpSignal[1:]
                    else:
                        print("Stopsingal received!\nEnding transmission...")
                        stopSigRecv = True
                        break
                time.sleep(2)
    if stopSigRecv:
        break
    time.sleep(2)
    client.disconnect()
client.disconnect()       

