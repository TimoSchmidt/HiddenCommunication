from opcua import Server
import time

server = Server()
# server address
url = "opc.tcp://127.0.0.1:4840"
server.set_endpoint(url)

name = "OPCServer"
addSpace = server.register_namespace(name)

# ns = 2
node = server.get_objects_node()
param = node.add_object(addSpace, "Parameters")

# i = 2
val1 = param.add_variable(addSpace, "Values1", 0)
val1.set_writable()

# initializing server
server.start()
print("Server is running")

# how many counts until the server stops
counter = 0

try:
    while True:
        # receives a value (here: temperature) from a client (e.g. a sensor)
        temperature = val1.get_value()
        val1.set_value(temperature)
        
        print(temperature)
        
        # condition to terminate the server       
        if(temperature == 11):
            counter = counter + 1
        if(counter == 3):
            server.stop()
                
        time.sleep(1)        
finally:    
    server.stop()    
    
    
