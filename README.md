# Team 3 - Stern

## About
The goal of this project is to control a robotic arm via a web interface. To proceed, we will send the values from the web interface to the server with HTTP POST requests, then the server will send the content of these requests via MQTT.


After that, there is a PC connected to the robot via an USB connection which will be receiving the MQTT messages and send them to the microcontroller via serial. 

Finally, the microcontroller updates its devices depending on the received messages, and transmits every 2 seconds its current values to the PC, which will be sent via MQTT to the server, written into a file, read by GET requests and updating the web interface.
## Setup

Just run "scripts-setup/server-setup.sh" to setup all you need on the server, and "scripts-setup/client-python-setup.sh" to setup the client side.
