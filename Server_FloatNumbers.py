from opcua import Server
import time

server = Server()
url = "opc.tcp://127.0.0.1:4840"
server.set_endpoint(url)
server.allow_remote_admin(1)

name = "OPCServer"
addSpace = server.register_namespace(name)

node = server.get_objects_node()
param = node.add_object(addSpace, "Parameters")

val1 = param.add_variable(addSpace, "Temperature", "")
val1.set_writable()

server.start()
print("Server is running")
nameSpace = server.get_namespace_array()
for ns in nameSpace:
    print(ns)

try:
    while True:
        temp = val1.get_value()
        if(val1.get_value() is not ""):
            print(temp[:5])
        time.sleep(0.5)    
finally:
    server.stop()