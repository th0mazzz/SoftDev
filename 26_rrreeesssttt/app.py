# Thomas Zhao
# Softdev pd8
# K26 -- 
# 2018-11-15

#This homework was made possible through the assistance of Aaron Li at the hours of 3:35PM to 5:55PM at the location known as WholeFoods Cafe.

#API key: KmUfLJ7wnHIVR9PMe2ha8SlYyWmnKMqYldGqziOp
#Example: https://api.nasa.gov/planetary/apod?api_key=KmUfLJ7wnHIVR9PMe2ha8SlYyWmnKMqYldGqziOp

from flask import Flask, render_template
import json, urllib

app = Flask(__name__)

##### Helper Functions #####
def meme():
    url="http://version1.api.memegenerator.net//Instances_Search?"
    apikey = "apikey=34b0833e-2bd7-4614-99d8-cec395f9c68c"
    
    httpresponse = urllib.request.urlopen(url) #this is initial httpresponse
    readresponse = httpresponse.read() #we are reading response
    decodedresponse = readresponse.decode() #we decode it for the json to load later
    #print(readresponse)

    data = json.loads(decodedresponse) #json loads this into usable dictionary
    return data

def help_func_name():
    url=""
    
    httpresponse = urllib.request.urlopen(url) #this is initial httpresponse
    readresponse = httpresponse.read() #we are reading response
    decodedresponse = readresponse.decode() #we decode it for the json to load later
    #print(readresponse)

    data = json.loads(decodedresponse) #json loads this into usable dictionary
    return data

############################

@app.route("/")
def root():
    nasa_data = nasa()
    quote_data = quote()
    return render_template("template.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
