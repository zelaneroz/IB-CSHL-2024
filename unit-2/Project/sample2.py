import numpy as np
import requests
from matplotlib import pyplot as plt
import warnings
warnings.simplefilter('ignore')

req = requests.get('http://192.168.6.142/readings')
data = req.json()
readings = data['readings'][0]
#DATA
temp = []
for sample in readings:
    if sample['sensor_id']==1:
        temp.append(sample['value'])
x = np.arange(0,400)
print(temp)
hum2 = temp[0:400]
#QUADRATIC MODEL y2
a,b,c = np.polyfit(x,hum2, 2)
for i in x:
    y2 = ((x**2)*a) + (b*x) + c

#LINEAR MODEL y3
m,b = np.polyfit(x,hum2, 1)
for i in x:
    y3 = (m*x)+b

#PLOTS
fig=plt.figure(figsize=(9,6))
plt.subplot(2,1,1) #DATA
plt.plot(temp)
plt.xlabel('Time')
plt.ylabel('Temperature')

plt.subplot(2,1,2) #MODEL
plt.scatter(x,hum2)
line1, = plt.plot(y3,c='green',label='Linear')
line2, = plt.plot(y2,c='red', label='Quadratic')
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.legend(handles=[line1, line2])

plt.tight_layout()
plt.show()