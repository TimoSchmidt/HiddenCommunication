from opcua import Client
from random import randint 
import time
import queue
from math import trunc
import sys

# returns str (more stable)
def truncate(f, n):
    #Truncates/pads a float f to n decimal places without rounding
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])
 
url = "opc.tcp://10.0.30.103:4840"
client = Client(url)

client.connect()
print("Client has connected succesfully")
#print("Avaialbe Namespaces: ", client.get_namespace_array())

dct = {
"a": "09","b": "15","c": "93","d": "49","e": "42","f": "77","g": "11","h": "89","i": "07","j": "76","k": "04","l": "33","m": "87","n": "03","o": "69","p": "55","q": "31","r": "81","s": "21","t": "74","u": "67","v": "99","w": "29","x": "61","y": "36","z": "26","A": "34","B": "18","C": "60","D": "85","E": "29","F": "13","G": "00","H": "14","I": "68","J": "35","K":"37","L": "75","M": "15","N": "02","O": "19","P": "30","Q": "64","R": "95","S": "59","T": "77","U": "40","V": "16","W": "01","X": "24","Y": "31","Z": "78","0": "20","1": "99","2": "84","3": "66","4": "05","5": "47","6": "43","7": "27","8": "56","9": "44",".": "88",",": "23", " ": "32"
}

queueie = queue.Queue()

string = input("Please enter your String: ") # sys.argv[1]
string = string + " "
#print(len(string))
def split(string):
    length = len(string)
    for i in range(0, length-1):
        cha = string[i]
        if cha in dct:
            var = dct.get(cha)
            queueie.put(var[0])
            queueie.put(var[1])
        else:
            var = dct.get(" ")
            queueie.put(var[0])
            queueie.put(var[1])

split(string)

tmp = client.get_node("ns = 2; i = 2")
#tmp.set_value("24.871")
print(list(queueie.queue))
while True:
    client.connect()
    for i in range(0, 1):
        tempC = client.get_node("ns = 2; i = 2")
        #print(tempC.get_value())
        val = tempC.get_value()[:-1]
        #print(val)
        tmp = queueie.get()
        res = val + tmp
        print(res + " " + tmp)
        queueie.put(tmp)
        tempC.set_value(res)
        time.sleep(2)
  
    client.disconnect()
    


