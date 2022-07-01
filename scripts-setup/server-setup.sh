#!/bin/bash

sudo yum upgrade -y
sudo yum install epel-release
sudo yum install fail2ban
sudo systemctl enable fail2ban
sudo systemctl restart fail2ban
sudo cat > /etc/fail2ban/jail.d/custom.conf << EOF
[DEFAULT]
ignoreip = 127.0.0.1
findtime = 10m
bantime = 10m
maxretry = 3
[sshd]
enabled = true
logpath = /var/log/auth.log
maxretry = 3
bantime = 10m
EOF
sudo yum install -y net-tools
sudo yum install -y firewalld
sudo systemctl enable firewalld
sudo systemctl restart firewalld
sudo firewall-cmd --add-port=22/tcp
sudo firewall-cmd --add-port=1935/tcp
sudo firewall-cmd --add-port=80/tcp
sudo firewall-cmd --add-port=1883/tcp
sudo firewall-cmd --reload
sudo yum install -y wget
sudo wget -O project.tar.gz 
http://gitlab.imerir.com/api/v4/projects/2804/repository/archive?private_token=glpat-6QdGrYxtbBovNAcjh7xm
sudo tar -xvzf project.tar.gz team3*
sudo rm -f project.tar.gz
sudo yum install -y docker
sudo mkdir container_python
sudo mkdir container_mqtt
sudo mv team3* container_python/final_project_adai
sudo cat > container_mqtt_broker/Dockerfile << EOF
FROM eclipse-mosquitto

RUN echo -e '\
team3:$7$101$dAxFlpAJ1/44zAKg$UFGliBg3jZqeQMZIIZhdAMln1nnxzlV92M3pdxjgq3RJT4Z/0sHl3NqY0okixcBOtMkXckWgIAmB4$
' >> mosquitto-pwd
RUN echo -e '\
listener 1883 172.17.0.4\n\
password_file mosquitto-pwd\
' >> mosquitto.conf

EXPOSE 1883/tcp
EOF
# Don't forget to run : mosquitto -c mosquitto.conf inside the container
sudo cat > container_python/Dockerfile << EOF
FROM python

RUN pip install flask
RUN pip install flask_cors
RUN pip install paho-mqtt

RUN mkdir -p /server/flask
RUN mkdir -p /server/mqtt

COPY final_project_adai/server/python/flask/ /server/flask
COPY final_project_adai/server/python/mqtt/ /server/mqtt


EXPOSE 80
EXPOSE 443

RUN python ~/flask/main.py & ~/mqtt/mqtt_client.py &
EOF
docker build -t "server-python" ./container_python/
docker build -t "mqtt-broker" ./container_mqtt_broker/
docker run -i -t -d -p 80:80 --name server-python server-python
docker run -d -p 1935:1935 --name rtmp-server tiangolo/nginx-rtmp
docker run -i -t -p 1883:1883 --name mqtt-broker mqtt-broker
echo "You're done, enter the MQTT container and run : mosquitto -c mosquitto.conf"
