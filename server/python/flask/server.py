import json
from flask import Flask, make_response, render_template, request
from flask_cors import CORS, cross_origin
import paho.mqtt.publish as publish

app = Flask(__name__);
CORS(app, resources={r"/*": {"origins":"*"}});

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api', methods = ['POST', 'GET'])

def api():
    if(request.method == 'GET'):
        try:
            data = "";
            with open("../mqtt/values.json", "r") as file:
                data = json.dumps(file);
                response = app.make_response(data);
                response.headers["Access-control-Allow-Origin"] = "*";
                return response;
        except IOError as error:
                response = app.make_response("Data couldn't be loaded");
                response.headers["Access-control-Allow-Origin"] = "*";
                return response;
    elif(request.method == 'POST'):
        #response = app.make_response('hello')
        #response.headers["Access-control-Allow-Origin"] = "*";
        data = request.get_json();
        publish.single(topic="control", payload = json.dumps(data) ,hostname="172.17.0.4", port=1883, client_id="Serveur", keepalive=60, auth={'username': 'team3', 'password': 'd*j-K5:BJK9;'});
        #with open("control.json", "w") as file:
         #   json.dump(data, file, indent=2);
        return("Page intended to be used with POST requests.")
    return("Page not intended to be used alone.")

if __name__ == '__main__':
        app.run(host="0.0.0.0", port=80, debug=True)