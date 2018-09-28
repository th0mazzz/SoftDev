# Thomas Zhao
# SoftDev pd8
# K13 -- Echo Echo Echo
# 2018-09-27

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def root():
    return render_template(
        'template.html', heading='Enter your username')

@app.route('/processing', methods=["GET", "POST"])
def process():
    return render_template(
        'return_template.html',
        user_name = request.args['username'],
        requestMethod = request.method,
        greeting = 'Hello, I am Thomaz! You successfully submitted the request! Here are the details of your request. Below is myself displaying pride for your success.')

@app.route('/print')
def prinT():
    
    print(app)
    print(request)
    print(request.args)
    print(request.method)
    return 'look at console'

if __name__ == '__main__':
    app.debug = True
    app.run()
