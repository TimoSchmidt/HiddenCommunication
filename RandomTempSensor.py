from opcua import Client
import random
import time

def convertCelToFahr(val):
    return ((val * 9/5) + 32)

def convertFahrToCel(val):
    return ((val - 32) * 5/9)

def truncate(f, n):
    '''Truncates/pads a float f to n decimal places without rounding'''
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])

url = "opc.tcp://127.0.0.1:4840"
client = Client(url)

client.connect()
print("Client has connected successfully ")
print("Available Namespaces: ", client.get_namespace_array())

try:
    while True:
        TempC = client.get_node("ns=2; i=2")
        TempF = client.get_node("ns=2; i=3")

        value = random.uniform(24,25.5)

        TempC.set_value(truncate(value,3))
        TempF.set_value(truncate(convertCelToFahr(value),3))
    
        time.sleep(10)
finally:
    client.disconnect()
