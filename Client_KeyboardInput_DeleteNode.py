from opcua import Client

# server address
url = "opc.tcp://127.0.0.1:4840"
client = Client(url)

client.connect()
print("Client connected")
    
try:
    # login, not saved yet
    user = input("Username: ")
    pwd = input("Password: ")
    print("Login successfully.")
    while True:      
        # get the server node
        inp = input("Your input: ")
        txt = client.get_node("ns = 2; i = 2")
        # set the node's value
        txt.set_value(inp)
        print(inp)
finally:
    client.disconnect()
