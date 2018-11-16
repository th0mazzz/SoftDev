# Thomas Zhao
# Softdev pd8
# K26 -- Getting More REST
# 2018-11-15

#This homework was made possible through the assistance of Aaron Li at the hours of 3:35PM to 5:55PM at the location known as WholeFoods Cafe.

#API key: KmUfLJ7wnHIVR9PMe2ha8SlYyWmnKMqYldGqziOp
#Example: https://api.nasa.gov/planetary/apod?api_key=KmUfLJ7wnHIVR9PMe2ha8SlYyWmnKMqYldGqziOp

from flask import Flask, render_template
import json, urllib, random

app = Flask(__name__)

##### Helper Functions #####
def meme():
    url = "http://version1.api.memegenerator.net//Instance_Select?"
    apikey = "apiKey=9ab0606e-e014-40b3-b9ee-bb8a4d713fa1"
    instanceid = "&instanceID=" + str(random.randrange(50, 53))
    fullurl = url + apikey + instanceid
    
    httpresponse = urllib.request.urlopen(fullurl) #this is initial httpresponse
    readresponse = httpresponse.read() #we are reading response
    decodedresponse = readresponse.decode() #we decode it for the json to load later
    print(readresponse)

    data = json.loads(decodedresponse) #json loads this into usable dictionary
    return data

def bored():
    url="https://www.boredapi.com/api/activity"
    
    httpresponse = urllib.request.urlopen(url) #this is initial httpresponse
    readresponse = httpresponse.read() #we are reading response
    decodedresponse = readresponse.decode() #we decode it for the json to load later
    #print(readresponse)

    data = json.loads(decodedresponse) #json loads this into usable dictionary
    return data

def norris():
    url="http://api.icndb.com/jokes/random"
    httpresponse = urllib.request.urlopen(url) #this is initial httpresponse
    readresponse = httpresponse.read() #we are reading response
    decodedresponse = readresponse.decode() #we decode it for the json to load later
    #print(readresponse)

    data = json.loads(decodedresponse) #json loads this into usable dictionary
    return data

############################

@app.route("/")
def root():
    meme_data = meme()
    bored_data = bored()
    norris_data = norris()
    return render_template("template.html",
                           meme_data=meme_data,
                           bored_data=bored_data,
                           norris_data=norris_data)

if __name__ == "__main__":
    app.debug = True
    app.run()
