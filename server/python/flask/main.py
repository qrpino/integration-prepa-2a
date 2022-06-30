import json
from flask import Flask, make_response, render_template, request
from flask_cors import CORS, cross_origin
import paho.mqtt.publish as publish
import os.path
# Let's create the Flask instance.
app = Flask(__name__);
# Let's define the CORS policy for http requests.
CORS(app, resources={r"/*": {"origins":"*"}});

@app.route('/')
def index():
    return render_template('index.html')

# Route created to handle XMLHttpRequests by the client.
@app.route('/api', methods = ['POST', 'GET'])
def api():
    if(request.method == 'GET'):
        try:
            # Prepare the GET request content.
            data = "";
            # Get the data from the file writen by the MQTT client running
            # on the server.
            with open(os.path.dirname(__file__) + "/../mqtt/values.json", "r") as file:
                # Store it into the data variable, which stays a String.
                data = json.load(file);
                response = app.make_response(data);
                # Set HTTP Headers to allow the server to process
                # XMLHttpRequests by all adresses.
                response.headers["Access-control-Allow-Origin"] = "*";
                return response;
            # If there was an error, send at least a response...
        except IOError as error:
                response = app.make_response("Data couldn't be loaded" + str(error));
                response.headers["Access-control-Allow-Origin"] = "*";
                return response;
    elif(request.method == 'POST'):
        # Get all the data from the POST request and JSONify it.
        data = request.get_json();
        # Send an MQTT message to our MQTT broker running on the same local network.
        # The message is a stringified JSON.
        publish.single(topic="control", payload = json.dumps(data) ,hostname="172.17.0.4", port=1883, client_id="Serveur", keepalive=60, auth={'username': 'team3', 'password': 'd*j-K5:BJK9;'});
        print(data);
        return("Page intended to be used with POST requests.")
    return("Page not intended to be used alone.")

if __name__ == '__main__':
    # Allow all adresses to access the HTTP server on the port 80, on debug mode.
        app.run(host="0.0.0.0", port=80, debug=True)