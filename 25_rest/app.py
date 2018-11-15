# Thomas Zhao
# Softdev pd8
# K25 -- Getting More REST
# 2018-11-15

#This homework was made possible through the assistance of Aaron Li at the hours of 3:35PM to 5:55PM at the location known as WholeFoods Cafe.

#API key: KmUfLJ7wnHIVR9PMe2ha8SlYyWmnKMqYldGqziOp
#Example: https://api.nasa.gov/planetary/apod?api_key=KmUfLJ7wnHIVR9PMe2ha8SlYyWmnKMqYldGqziOp

from flask import Flask, render_template
import json, urllib

app = Flask(__name__)

##### Helper Functions #####
def nasa():
    url="https://api.nasa.gov/planetary/apod?api_key=KmUfLJ7wnHIVR9PMe2ha8SlYyWmnKMqYldGqziOp&date=2018-11-12&hd=True"
    
    httpresponse = urllib.request.urlopen(url) #this is initial httpresponse
    readresponse = httpresponse.read() #we are reading response
    decodedresponse = readresponse.decode() #we decode it for the json to load later
    #print(readresponse)

    data = json.loads(decodedresponse) #json loads this into usable dictionary
    return data

def quote():
    url="https://favqs.com/api/qotd"

    httpresponse = urllib.request.urlopen(url) #this is initial httpresponse
    readresponse = httpresponse.read() #we are reading response
    decodedresponse = readresponse.decode() #we decode it for the json to load later
    #print(readresponse)

    data = json.loads(decodedresponse) #json loads this into usable dictionary
    print(data)
    return data

############################

@app.route("/")
def root():
    nasa_data = nasa()
    quote_data = quote()
    return render_template("template.html", nasa_data=nasa_data, quote_data=quote_data)

if __name__ == "__main__":
    app.debug = True
    app.run()
