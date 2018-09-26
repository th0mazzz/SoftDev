import random
#the mechanism behind our random selection
# picking an occupation code

def readFile():
    file = open('data/occupations.csv','r')
    info = file.read().split("\n")
    file.close()
    
    info.pop(0) # Title line
    info.pop(len(info)-1) # Last line
    info.pop(len(info)-1) # again due to some issue with csv
    return info

def initDict():
    # Initialize dictionary
    info = readFile()
    book = {}
    for entry in range(0,len(info)):
        if info[entry].count(',') == 2:
            line = info[entry].split(",")
            book[line[0]] = (float(line[1]), line[2])
        else: 
            # more than 2 commas
            storage = info[entry].split('"') #splits by double quote character
            storage.remove('')               #removes empty string element
            resplit = storage[1].split(',')  #splits num&link element by comma
            resplit.remove('')               #removes empty string elements
            storage.append(resplit)          #adds the two lists together
            storage.pop(1)                   #removes useless element 
            #storage's format is [name, [number, link] ]

            book[storage[0]] = (float(storage[1][0]), storage[1][1]) #creation of key, tuple pair
            #book's format is {name: (number, link) ... }
    return book

def pickOccupation(): 
    
    book = initDict()
    
    target = random.uniform(0, 99.8)
    current = 0
    
    for entry in book: #keep adding job percent values until it is higher than targetx
        current = current + book[entry][0]
        if current > target:
            return entry,book
        
