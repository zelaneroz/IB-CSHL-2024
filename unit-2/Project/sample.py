import matplotlib.pyplot as plt
import requests
import numpy as np
import warnings
warnings.simplefilter('ignore')

req = requests.get('http://192.168.6.142/readings')
data = req.json()
readings = data['readings'][0]
hum,temp =[],[]

for sample in readings:
    if sample['sensor_id']==5:
        temp.append(sample)
    if sample['sensor_id']==4:
        hum.append(sample)

def times(hum): #GETS THE SPECIFIC TIMES THE LOCAL SERVER ALSO STARTED RECORDING
    sample2 = []
    for i in hum:
        if int(i['datetime'][8:10])==9 and int(i['datetime'][11:13])>21:
            sample2.append(i['value'])
        elif int(i['datetime'][8:10])>9:
            #sample2.append(i)
            sample2.append(i['value'])
    return sample2

hum = times(hum)[:576]
temp = times(temp)[:576]

plt.subplot(2,1,2)
plt.plot(hum)
plt.title("Remote - Humidity")
plt.subplot(2,1,1)
plt.plot(temp)
plt.title("Remote - Temperature")
plt.tight_layout()
plt.show()