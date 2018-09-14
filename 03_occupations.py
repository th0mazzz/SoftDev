# Wei Wen Zhou
# SoftDev1 pd8
# K#06: StI/O: Divine your Destiny!
# 2018-09-13

import random

file = open("occupations.csv",'r')
info = file.read().split("\n")
file.close()

print(info)
print(len(info))
info.pop(0) # Title line
print(info)
print(len(info))
info.pop(len(info)-1) # Last line
print(info)
print(len(info))
print("yeaadjaefewnfnfewiofl")

# Initialize dictionary
book = {}
print(len(info))
for index in range(0,len(info)):
    if info[index].count(',') == 1:
        line = info[index].split(",")
        book[line[0]] = float(line[1])
    else: 
    # more than 1 comma
        lastC = info[index].rindex(',')
        book[info[index][0:lastC]] = float(info[index][lastC+1:len(info[index])-1])

names = []
weights = []
        
for key, value in book.iteritems():
    i = 0
    names.append(key)
    weights.append(value)

print(random.choices(names, weights, k=1))

