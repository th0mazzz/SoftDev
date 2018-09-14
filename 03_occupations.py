# Wei Wen Zhou, Thomas Zhao
# SoftDev1 pd8
# K#06: StI/O: Divine your Destiny!
# 2018-09-13
# Team Double Z Dynasty

import random

def pickOccupation():
    file = open("occupations.csv",'r')
    info = file.read().split("\n")
    file.close()
    
    info.pop(0) # Title line
    info.pop(len(info)-1) # Last line
    info.pop(len(info)-1) # again due to some issue with csv
    
    # Initialize dictionary
    book = {}
    for index in range(0,len(info)):
        if info[index].count(',') == 1:
            line = info[index].split(",")
            book[float(line[1])] = (line[0])
        else: 
            # more than 1 comma
            lastC = info[index].rindex(',')
            book[float(info[index][lastC+1:len(info[index])-1])] = info[index][0:lastC]
             
    print(book)

    #debug
    all = 0
    for key in book:
        all = all + float(key)
    print(all)
    #debug
    
    target = random.uniform(0, 99.8)
    print(target)
    total = 0
    
    for key in book:
        total = total + float(key)
        print(total)
        if total > target:
            print(book[key])
            return book[key]

        
    #return(random.choices(names, weights, k=1))

print(pickOccupation())
