import json
from flask import Flask, render_template, request
from flask_cors import CORS
import paho.mqtt.publish as publish

app = Flask(__name__);
CORS(app, resources={r"/*": {"origins":"*"}});

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api', methods = ['POST', 'GET'])
def api():
    if(request.method == 'GET'):
        pass;
    elif(request.method == 'POST'):
        data = request.get_json();
        #publish.single(topic="control", payload = json.dump(data) ,hostname="stern3.imerir.org", port=8883, client_id="Serveur", keepalive=60, auth={'username':'', 'password':''});
        with open("control.json", "w") as file:
            json.dump(data, file, indent=2);
        return("Post page, nothing to do here")