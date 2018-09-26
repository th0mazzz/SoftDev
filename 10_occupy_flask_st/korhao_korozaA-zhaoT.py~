#Aleksandra Koroza, Thomas Zhao
#SoftDev1 pd8
#K #10: Jinja Tuning 
#2018-09-23 

from flask import Flask,render_template
from util import occupations
app = Flask(__name__) #create instance of class Flask

@app.route("/")
def not_here():
    return "please type in occupations into the url to get a job!"


@app.route("/occupations")
def hello_world(): #assign fxn to route
    occ,book = occupations.pickOccupation()
    return render_template(
        'text.html',
        randomOcc = occ,
        collection = book
        )


if __name__ == "__main__":
    app.debug = True
    app.run()

