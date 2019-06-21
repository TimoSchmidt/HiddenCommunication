from opcua import Client
import time

dct = {
"328": "a","090": "b","648": "c","977": "d","778": "e","324": "f","709": "g","351": "h","818": "i","370": "j","933": "k","810": "l","897": "m","573": "n","409": "o","548": "p","173": "q","849": "r","383": "s","169": "t","736": "u","124": "v","296": "w","715": "x","508": "y","504": "z","291": "A","661": "B","354": "C","281": "D","847": "E","823": "F","429": "G","222": "H","567": "I","111": "J","878": "K","463": "L","170": "M","844": "N","983": "O","655": "P","598": "Q","419": "R","979": "S","268": "T","928": "U","795": "V","056": "W","022": "X","270": "Y","953": "Z","596": "0","304": "1","752": "2","903": "3","315": "4","714": "5","677": "6","431": "7","342": "8","868": "9","501": ".","217": ",","806": " "
}

url = "opc.tcp://10.0.30.103:4840"
client = Client(url)


print("Client has connected succesfully")
#print("Avaialbe Namespaces: ", client.get_namespace_array())

val = ""
counter = 0
while True:
    client.connect()   
    if counter <= 2:
        recMes = client.get_node("ns = 2; i = 2")
        val = val + recMes.get_value()[-1:]
        counter = counter + 1
        print("test: ", val)
    if counter == 3:
        if val in dct:
            print("Message contains: " + dct.get(val))
            val = ""
            counter = 0
        else:
            val = val[-2:]
            counter = counter - 1
    time.sleep(2)
    client.disconnect()    
    
    ''' alternativ
    client.connect()   
    for i in range(3):
        if counter <= 2:
            recMes = client.get_node("ns = 2; i = 2")
            val = val + recMes.get_value()[-1:]
            counter = counter + 1
            print("test: ", val)
        if counter == 3:
            if val in dct:
                print("Message contains: " + dct.get(val))
                val = ""
                counter = 0
            else:
                val = val[-2:]
                counter = counter - 1
        # time.sleep(2) // Original
        time.sleep(0.65)
    client.disconnect()    
    time.sleep(8)
    '''
    
        

