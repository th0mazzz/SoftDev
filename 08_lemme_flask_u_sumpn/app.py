#Thomas Zhao
#SoftDev pd8
#K#08 -- Fill Yer Flask
#2018-09-19

from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'hello, welcome to the flask app by tzhao2. <br><br> add "/cat" to this url for cats. <br>add "/dog" to the end of the url for dogs. <br><br> or you can click the hyperlinks i guess.<br><br> <a href="/cat">click here for cat page</a><br><a href="/dog">click here for dog page</a>'

@app.route('/cat')
def cat_page():
    return '<a href="https://en.wikipedia.org/wiki/Cat">this is what a cat is</a>'

@app.route('/dog')
def dog_page():
    return '<a href=https://en.wikipedia.org/wiki/Dog>this is what a dog is</a>' + '<br>' + '<a href="https://en.wikipedia.org/wiki/Cat">this is not what a dog is</a>'

if __name__ == '__main__':
    app.debug = True
    app.run()
