temp = []
hum = []
#1: EXTRACTING THE VALUE
# Create a loop until range 101

import serial
import time
from matplotlib import pyplot as plt
import warnings
warnings.simplefilter('ignore')
arduino = serial.Serial(port='/dev/cu.usbserial-1120', baudrate=9600, timeout=.1)

def read():
    data = ""
    while len(data)<1:
        data = arduino.readline()
    return data

for i in range(5):
    time.sleep(0.1)
    value = read() #wait until data is in the port
    msg = value.decode('utf-8')
    print(msg)
    msg=msg.split(" ")
    print(msg)
    hum.append(msg[0][9:14])
    temp.append(msg[1][12:17])

print("-- Data Collected -- ")
print(temp)
print(hum)
plt.ylabel('Humidity')
plt.xlabel('Temperature')
plt.scatter(temp,hum)
plt.show()

