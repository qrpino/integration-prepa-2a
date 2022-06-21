from crypt import methods
import string
from flask import Flask, flash, render_template, request

app = Flask(__name__);

@app.route('/', methods = ['POST', 'GET'])
def index():
    data = None;
    if(request.method == 'POST'):
        data = {};
        
        data['mode'] = request.form['mode'];
        if request.form.get('mode') == 0:
            pass;
        else:
            if int(request.form["points-count"]) > 0:
                data["points"] = [];
                for i in range(1, int(request.form["points-count"]) + 1):
                    data["points"].append((request.form["point-"+str(i)+"-x"], request.form["point-"+str(i)+"-y"]))
                    pass;
        pass;
    elif(request.method == 'GET'):
        pass;
    return render_template('index.html', data = data);