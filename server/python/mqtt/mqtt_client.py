import json
import threading
#import paho.mqtt.client as MQTT
import requests

#session = MQTT.Client(client_id="vini-serial")
#def on_log( client, userdata, level, buf ):
#    print( "log: ", buf)

#def on_connect( client, userdata, flags, rc ):
#    print( "Connexion: code retour = %d" % rc )
#    print( "Connexion: Statut = %s" % ("OK" if rc==0 else "Echec connection") )
#    client.subscribe("Message_Serveur")

#def on_message(client, userdata, message):
#    print(message.payload)


#def init(adress, port, refreshRate):
#    session.connect(host=adress, port=port, keepalive=refreshRate)
#    session.on_connect = on_connect
#    session.on_log = on_log
#    session.on_message = on_message

#init('77.159.224.22', 8883, 50)
#threading.Thread(target=session.loop_forever).start()


print(json.loads(requests.get('http://127.0.0.1:5000/api?state=?').text))