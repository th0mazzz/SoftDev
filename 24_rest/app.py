# Thomas Zhao
# Softdev pd8
# K24 -- A RESTful Journey Skyward
# 2018-11-13

#this is your API key: KmUfLJ7wnHIVR9PMe2ha8SlYyWmnKMqYldGqziOp
#this is their example: https://api.nasa.gov/planetary/apod?api_key=KmUfLJ7wnHIVR9PMe2ha8SlYyWmnKMqYldGqziOp

from flask import Flask
app = Flask(__name__)

@app.route("/")
def root():
    return "No hablo queso!"

if __name__ == "__main__":
    app.debug = True
    app.run()
