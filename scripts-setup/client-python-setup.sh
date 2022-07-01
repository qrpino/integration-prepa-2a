sudo apt-get install python3
python3 -m pip install paho-mqtt
python3 -m pip install flask
python3 -m pip install flask_cors
python3 -m pip install pyserial
sudo chmod -R -660 /dev/ttyUSB*
sudo chmod -R -660 /dev/ttyACM*
sudo apt-get install wget
sudo wget -O project.tar.gz http://gitlab.imerir.com/api/v4/projects/2804/repository/archive?private_token=glpat-6QdGrY$
sudo tar -xvzf project.tar.gz team3*
sudo mv team3* final_project_adai
python3 final_project_adai/client/python/main.py
