from opcua import Client
import time

url = "opc.tcp://127.0.0.1:4840"
client = Client(url)

client.connect()
print("Client has connected successfully")




print("Hello Walter")
counter = 0
flag = False


while True:
    in_message = input("Please acknowledge ")
    try:
        in_message = int(in_message)
        if(in_message==8):
            counter = counter+1
            print("Achnowledges left", 3-counter)
            if(counter == 3):
                print('successfully acknoledged')
                flag = True
                break
    except ValueError:
        print("This is not a valid number ")

if(flag == True):
	print('From Server disconnected')
	client.disconnect()
