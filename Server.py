from opcua import Server
import datetime
from random import randint
import time


server = Server()
url = "opc.tcp://127.0.0.1:4840"
server.set_endpoint(url)
print("[DEBUG] SUCCESS SERVER CHECKED...SERVER IS LISTING ON:", url)
server.allow_remote_admin(1)

name = "OPCSERVER"
addspace = server.register_namespace(name)

node = server.get_objects_node()

Param = node.add_object(addspace, "Parameters")

Temp = Param.add_variable(addspace, "Temperature", 0)
Press = Param.add_variable(addspace, "Pressure", 0)
Time = Param.add_variable(addspace, "Time", 0)

Temp.set_writable()
Press.set_writable()
Time.set_writable()



server.start()
print("Server started")

while True:
    Temperature = randint(40, 50)
    Pressure = randint(200, 300)
    TIME = datetime.datetime.now()


    print("Current Temperature: ",Temperature, "Current Pressure: ", Pressure, "TimeStamp ", TIME)

    Temp.set_value(Temperature)
    Press.set_value(Pressure)
    Time.set_value(TIME)

    time.sleep(2)
