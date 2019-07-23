from opcua import Client
import time
import spidev
import os
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

    # Function to read SPI data from MCP3008 chip
def ReadChannel(channel):
    adc = spi.xfer2([1,(8+channel)<<4,0])
    data = ((adc[1]&3) << 8) + adc[2]
    return data

def ConvertVolts(data,places):
  volts = (data * 3.3) / 1023
  volts = round(volts,places)
  return volts


def ConvertTemp(data,places):

  # ADC Value
  # (approx)  Temp  Volts
  #    0      -50    0.00
  #   78      -25    0.25
  #  155        0    0.50
  #  233       25    0.75
  #  310       50    1.00
  #  465      100    1.50
  #  775      200    2.50
  # 1023      280    3.30

  temp = ((data * 330)/float(1023))-50
  temp = round(temp,places)
  return temp


GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)


spi = spidev.SpiDev()           # create spi object
spi.open(0,0)                   # open spi port 0, device (CS) 0
spi.max_speed_hz=1000000

# Define sensor channels
#light_channel = 0
temp_channel  = 1

file = open("Sensordaten82.txt", "w")

url = "opc.tcp://192.168.178.53:4840"
client = Client(url)

client.connect()
print("Client has connected successfully ")
print("Available Namespaces: ",client.get_namespace_array())
sec = 0; 

while True:
    client = Client(url)
    client.connect()
    temp_level = ReadChannel(temp_channel)
    temp_volts = ConvertVolts(temp_level,2)
    temp       = (ConvertTemp(temp_level,3))*0.1

    TempC = client.get_node("ns=2; i=2")
    TempF = client.get_node("ns=2; i=3")

    GPIO.output(8, GPIO.HIGH)
    #value = random.uniform(5,10)

    TempC.set_value(truncate(temp,3))
    TempF.set_value(truncate(convertCelToFahr(temp),3))
    file.write("{0:.1f}".format(sec) + " " + str(temp) +"\n")
    sec = sec+10
    GPIO.output(8, GPIO.LOW)
    client.disconnect()
    time.sleep(10)
