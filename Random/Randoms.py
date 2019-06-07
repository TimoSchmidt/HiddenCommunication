from random import randint
import string

var = list(string.ascii_letters)
for i in range (10):
    var.append(str(i))

var.append('.')
var.append(',')

file = open("rand.txt", "w")

file.write("dct = {\n")
for i in var:
    file.write("\"" + str(randint(0,9)) + str(randint(0, 9)) + "\": \"" + i + "\", \n")
file.write("}")

