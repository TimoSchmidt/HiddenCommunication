from random import randint
from collections import Counter
import string

var = list(string.ascii_letters)
for i in range (10):
    var.append(str(i))

var.append('.')
var.append(',')
var.append(' ')

file = open("rand.txt", "w")
file.write("dct = {\n")

li = []

for i in var:
    # changed to 3 random numbers
    rand = str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9))
    li.append(rand)
    file.write("\"" + rand + "\": \"" + i + "\",")

file.write("\n}\n\n")

# Erkennung von Duplikaten
li.sort()
'''
file.write("[")
for l in li:
    file.write(l + ", ")
file.write("]\n\n")
'''

counter = 0
total = 0
for j in li:
    for k in li:
        if(j == k):
            counter = counter + 1
    if(counter >= 2):
        file.write(j + ": " + str(counter) + "\n")
        total = total + counter
    counter = 0
file.write("Total duplicates = " + str(total) + "\n")




