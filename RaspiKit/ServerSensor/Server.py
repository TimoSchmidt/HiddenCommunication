from opcua import Server
import datetime
from random import randint
import time

file = open("ServerPrinzipAlle82.txt","w")

server = Server()

url = "opc.tcp://192.168.178.53:4840"

server.set_endpoint(url)
print("SUCCESS SERVER CHECKED...SERVER IS LISTING ON:", url)
server.allow_remote_admin(1)

name = "OPCSERVER_PARAMS_PI"
addspace = server.register_namespace(name)

node = server.get_objects_node()

Param = node.add_object(addspace, "Parameters")


Temp = Param.add_variable(addspace, "TemperatureC", "0")
TempF = Param.add_variable(addspace, "TemperatureF", "0")

Time = Param.add_variable(addspace, "Time", 0)

Temp.set_writable()
TempF.set_writable()
Time.set_writable()



server.start()
print("Server started")
nameSpace = server.get_namespace_array()
print("Current Namespace on Server: ", nameSpace[2])
print("-----------------------------------------------")

sec = 0.0
while True:

    TIME = datetime.datetime.now()
    temperature = Temp.get_value()
    Temp.set_value(temperature)
    temperatureF = TempF.get_value()
    TempF.set_value(temperatureF)
    print("Temperature: ",temperature ,"°C", "|",temperatureF, "°F ","TimeStamp ", TIME)
    file.write("{0:.1f}".format(sec) + " " + str(temperature)+"\n")
    sec = sec+0.1

    Time.set_value(TIME)

    time.sleep(0.1)
