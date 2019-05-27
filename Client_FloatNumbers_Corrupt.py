from opcua import Client
import random
import time
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
url = "opc.tcp://127.0.0.1:4840"
client = Client(url)

client.connect()
print("Client has connected succesfully")
#print("Avaialbe Namespaces: ", client.get_namespace_array())

counter = 0
# helloworld reversed (in order to use pop)
lst = ["4", "12", "18", "15", "23", "15", "12", "12", 
       "5", "8"]
# yippieyahyeischweinebacke
lst2 = ["5", "11", "3", "1", "2", "5", "14", "9", "5", "23", "8", "3", "19", 
        "9", "5", "25", "8", "1", "25", "5", "9", "16", "16", "9", "25"]
try:
    while True:
        tempC = client.get_node("ns = 2; i = 2")
        val = truncate(random.uniform(5, 10), 3)
        if(counter is 10 and lst):
            #tempC.set_value(val + lst.pop())
            tempC.set_value(val + lst2.pop())
            counter = 0
        else:
            tempC.set_value(val)
            counter = counter + 1
        print(val)
        time.sleep(0.5)
finally:
    client.disconnect()