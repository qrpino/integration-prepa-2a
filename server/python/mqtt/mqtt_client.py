import paho.mqtt.client as mqtt
import json

def on_message(client, userdata, message):
    try:
        json.loads(message.decode('utf-8'));
        with open("values.json", "w") as file:
            file.write(message.payload.decode('utf-8'));
    except ValueError as error:
        pass;
    
def on_connect(client, userdata, flags, rc):
    client.subscribe(topic="values");
    
mqtt_client = mqtt.Client(client_id="server");
mqtt_client.on_message = on_message;
mqtt_client.on_connect = on_connect;
mqtt_client.username_pw_set("team3", "d*j-K5:BJK9;");
mqtt_client.connect(host="172.17.0.4", port=1883, keepalive=60);

mqtt_client.loop_forever();