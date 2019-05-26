from opcua import Server
import time

server = Server()
url = "opc.tcp://127.0.0.1:4840"
server.set_endpoint(url)

name = "OPCServer"
addSpace = server.register_namespace(name)

# ns = 2
node = server.get_objects_node()
param = node.add_object(addSpace, "Parameters")

# i = 2
val1 = param.add_variable(addSpace, "Values1", "")
val1.set_writable()

# initializing server
server.start()
print("Server is running")

try:
    # shutdown server
    counter = 0
    while True:
        # Input string from client
        txt = val1.get_value()
        val1.set_value(txt)
        # delete node if string matches
        if("test" in txt):
            node.delete()
        print(txt)
        time.sleep(2)
finally:
    server.stop()        
    
