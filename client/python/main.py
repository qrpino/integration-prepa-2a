import paho.mqtt.client as mqtt
from time import sleep
import serial_enum
import serial
import json
import threading

# Serial Init --------------------------------
serialPorts = serial_enum.main()
portHandle = int(input("What port do you want to use ? (1 for first, 2 for second...)")) - 1;
baudRate = int(input("What is the baudrate of the device ? "));
"""
serialHandle = serial.Serial(port=serialPorts[portHandle], baudrate=baudRate, timeout=1);
"""
def writeToSerialPort(message):
    with serial.Serial(port=serialPorts[portHandle], baudrate=baudRate, timeout=1) as serialHandle:
        serialHandle.write(bytes(message, 'ascii'));
# ----------------------------------------------------------------

# MQTT Client setup ----------------------------------------------------------------
def on_message(client, userdata, message):
    try:
        msg = json.loads(message.payload.decode('ascii'));
        writeToSerialPort(message.payload.decode('ascii'));
        print(message.payload.decode('ascii'));
    except ValueError as error:
        print("Bad format from arduino: " + message.payload.decode('ascii'));

def on_connect(client, userdata, flags, rc):
    client.subscribe("control");
    
mqtt_client = mqtt.Client(client_id="serial_pc");
mqtt_client.on_message = on_message;
mqtt_client.on_connect = on_connect;
mqtt_client.username_pw_set("team3", "d*j-K5:BJK9;");
mqtt_client.connect(host="stern3.imerir.org", port=8883, keepalive=60);
# -------------------------------------------------------------------        
def listenSerial():
    with serial.Serial(port=serialPorts[portHandle], baudrate=baudRate, timeout=0.05) as serConn:
        sleep(1);
        while True:
            serialMsg = serConn.readall().decode('utf-8');
            if(len(serialMsg) > 0):
                try:
                    jsonMsg = json.loads(serialMsg.replace("'", '"'));
                    mqtt_client.publish(topic="values", payload=serialMsg);
                except ValueError as e:
                    print(serialMsg);

def testMessages():
    while True:
        messageToSend = input("Send motor values JSON Format");
        jsonized = json.loads(messageToSend);
        mqtt_client.publish(topic="values", payload=json.dumps(jsonized));
        
threading.Thread(target=listenSerial).start();
threading.Thread(target=mqtt_client.loop_forever).start();
