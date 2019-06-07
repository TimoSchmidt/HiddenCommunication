from opcua import Client
from random import randint 
import time
import queue
from math import trunc

# returns str (more stable)
def truncate(f, n):
    #Truncates/pads a float f to n decimal places without rounding
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])
'''
# returns float (not stable due to the imperfection of floats)
def truncate(number, decimals):
    if decimals < 0:
        raise ValueError('truncate received an invalid value of decimals ({})'.format(decimals))
    elif decimals == 0:
        return trunc(number)
    else:
        factor = float(10**decimals)
        return trunc(number*factor)/factor
'''    
url = "opc.tcp://10.0.21.175:4840"
client = Client(url)

client.connect()
print("Client has connected succesfully")
#print("Avaialbe Namespaces: ", client.get_namespace_array())

queueie = queue.Queue()
lst = ["0", "0", "4", "2", "8", "7", "8", "7", "6", "6"]
for i in lst:
    queueie.put(i)

tmp = client.get_node("ns = 2; i = 2")
tmp.set_value("24.871")
while True:
    for i in range(0, 1):
        tempC = client.get_node("ns = 2; i = 2")
        val = tempC.get_value()[:-1]
        tmp = queueie.get()
        res = val + tmp
        queueie.put(tmp)
        print(res)
        tempC.set_value(res)
        time.sleep(0.5)
    time.sleep(5)

