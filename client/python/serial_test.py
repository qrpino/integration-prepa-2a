from time import sleep
import serial_enum
import serial

serialPorts = serial_enum.main()
portHandle = int(input("What port do you want to use ? (1 for first, 2 for second...)")) - 1;
baudRate = int(input("What is the baudrate of the device ? "));


message1 = '''{"motors" : [120, 180, 160, 20]}'''

while True:
    serialHandle = serial.Serial(port=serialPorts[portHandle], baudrate=baudRate);
    serialHandle.reset_input_buffer();
    serialHandle.reset_output_buffer();
    serialHandle.write(bytes(message1, 'ascii'));
    sleep(2);