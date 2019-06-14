from opcua import Client
import time

dct = {
"09": "a","15": "b","93": "c","49": "d","42": "e","77": "f","11": "g","89": "h","07": "i","76": "j","04": "k","33": "l","87": "m","03": "n","69": "o","55": "p","31": "q","81": "r","21": "s","74": "t","67": "u","99": "v","29": "w","61": "x","36": "y","26": "z","34": "A","18": "B","60": "C","85": "D","29": "E","13": "F","00": "G","14": "H","68": "I","35": "J","37": "K","75": "L","15": "M","02": "N","19": "O","30": "P","64": "Q","95": "R","59": "S","77": "T","40": "U","16": "V","01": "W","24": "X","31": "Y","78": "Z","20": "0","99": "1","84": "2","66": "3","05": "4","47": "5","43": "6","27": "7","56": "8","44": "9","88": ".","23": ",", "32": " "

}
url = "opc.tcp://10.0.30.103:4840"
client = Client(url)

client.connect()
print("Client has connected succesfully")
#print("Avaialbe Namespaces: ", client.get_namespace_array())

val = ""
while True:
    recTempC = client.get_node("ns = 2; i = 2")
    val = val + recTempC.get_value()[-1:]
    print("test: ", val)
    if(val in dct):
        print(dct.get(val))
        val = ""
    else:
        val = val[-1:]
    time.sleep(2)
    
        

