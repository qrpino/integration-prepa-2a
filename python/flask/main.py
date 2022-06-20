from crypt import methods
from flask import Flask, flash, render_template, request

app = Flask(__name__);

@app.route('/', methods = ['POST', 'GET'])
def index():
    data = None;
    if(request.method == 'POST'):
        pass;
    elif(request.method == 'GET'):
        pass;
    return render_template('index.html', data = data);