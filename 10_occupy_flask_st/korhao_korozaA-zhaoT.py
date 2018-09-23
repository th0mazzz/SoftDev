#Aleksandra Koroza, Thomas Zhao
#SoftDev1 pd8
#K #10: Jinja Tuning 
#2018-09-23 

from flask import Flask,render_template
import random, os
app = Flask(__name__) #create instance of class Flask

# picking an occupation code
def pickOccupation():
    file = open(os.getcwd()+"/data/occupations.csv",'r')
    info = file.read().split("\n")
    file.close()
    
    info.pop(0) # Title line
    info.pop(len(info)-1) # Last line
    info.pop(len(info)-1) # again due to some issue with csv
    
    #print('info length:')
    #print(len(info))
    
    # Initialize dictionary
    book = {}
    for x in range(0,len(info)):
        if info[x].count(',') == 2:
            line = info[x].split(",")
            book[line[0]] = (float(line[1]), line[2])
        else: 
            # more than 2 commas
            storage = info[x].split('"') #splits by "
            storage.remove('') #removes '' element
            resplit = storage[1].split(',') #splits num&link element by ,
            resplit.remove('') #removes '' elements
            storage.append(resplit)
            storage.pop(1) #removes useless element 
            #storage's format is [name, [number, link] ]

            book[storage[0]] = (float(storage[1][0]), storage[1][1])
            #book's format is {name: (number, link) ... }

    target = random.uniform(0, 99.8)
    current = 0

    print(book)
    
    for entry in book:
        current = current + book[entry][0]
        if current > target:
            return entry,book
        

@app.route("/occupations")
def hello_world(): #assign fxn to route
    f,b= pickOccupation()
    return render_template(
        'text.html',
        foo = f,
        c = b
        )


if __name__ == "__main__":
    app.debug = True
    app.run()

