from opcua import Client
import time
import random
import RPi.GPIO as GPIO


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


GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)


url = "opc.tcp://192.168.0.109:4840"
client = Client(url)

client.connect()
print("Client has connected successfully ")
print("Available Namespaces: ",client.get_namespace_array())

while True:
    TempC = client.get_node("ns=2; i=2")
    TempF = client.get_node("ns=2; i=3")

    GPIO.output(8, GPIO.HIGH)
    value = random.uniform(5,10)

    TempC.set_value(truncate(value,3))
    TempF.set_value(truncate(convertCelToFahr(value),3))
    GPIO.output(8, GPIO.LOW)
    time.sleep(1)
