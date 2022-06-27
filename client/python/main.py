import threading
import json
from time import sleep
import requests
import serial_enum
import serial
import paho.mqtt.client as mqtt

# FUNCTIONS DEFINITIONS #
# SERIAL #
def serialConn():
    serialPorts = serial_enum.main()
    portHandle = int(input("What port do you want to use ? (1 for first, 2 for second...)")) - 1;
    baudRate = int(input("What is the baudrate of the device ? "));
    return serial.Serial(port=serialPorts[portHandle], baudrate=baudRate)

def serialListenLoop(p_serialHandle: serial.Serial):
    while True:
        sleep(1);
        try:
            # Regex + JSON
            p_serialHandle.read_all();
            # Send MQTT Message if valid read
        except ValueError:
            print("Invalid data from serial");
# HTTP REQUESTS #
def fetch(method, url, data):
    response = None;
    if(method == "GET"):
        try:
            response = json.load(requests.get(url=url+data));
        except ValueError:
            return None
    elif(method == "POST"):
        try:
            response = requests.post(url=url, params=data);
        except ValueError:
            return None
# MQTT #
def on_connect( client, userdata, flags, rc ):
    print("Connexion: code retour = %d" % rc );
    print("Connexion: Statut = %s" % ("OK" if rc==0 else "Echec connection"));
    client.subscribe("Message_Serveur");

def handleOnMessage(client, userdata, message):
    try:
        payload = json.loads(message.payload.decode('utf-8'));
        serialHandle.write(payload.encode('utf-8'));
    except ValueError:
        print('JSON Error');
# END FUNCTIONS DEFINITIONS #

serialHandle = serialConn();

mqttHandle = mqtt.Client(client_id="arduino-serial")
mqttHandle.on_connect = on_connect;
mqttHandle.on_message = handleOnMessage;
mqttHandle.connect(host="stern3.imerir.org", port=8883, keepalive=60);



threading.Thread(target=)
