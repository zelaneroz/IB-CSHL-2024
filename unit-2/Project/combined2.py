import matplotlib.pyplot as plt
import requests
import numpy as np
import warnings
warnings.simplefilter('ignore')
from matplotlib import ticker

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
    #START TIME
        if i['datetime'][8:10] =='09' and i['datetime'][11:13] == '21' and int(i['datetime'][14:16]) in range(35,60):
            sample2.append(i['value'])
        elif i['datetime'][8:10] in ['10','11']:
            sample2.append(i['value'])
    #END_TIME
    #elif i['datetime'][8:10] =='11' and int(i['datetime'][11:13]) in range(0,22) and int(i['datetime'][14:16]) in range(0,36):
    #    sample2.append(i)
    return sample2

hum = times(hum)
temp = times(temp)


req = requests.get('http://192.168.6.142/readings')
data1 = req.json()
readings = data1['readings'][0]

pins = {'Sensor 1':[452,467],'Sensor 2':[464,468],'Sensor 3':[465,469],'Sensor 4':[466,471]}
data = {'Sensor 1':{'temp':[],'humidity':[]},'Sensor 2':{'temp':[],'humidity':[]}, 'Sensor 3':{'temp':[],'humidity':[]},'Sensor 4':{'temp':[],'humidity':[]}}

for sample in readings:
    for k in data.keys():
        if sample['sensor_id'] == pins[f'{k}'][0]:
            data[f'{k}']['temp'].append(sample['value'])
        elif sample['sensor_id'] == pins[f'{k}'][1]:
            data[f'{k}']['humidity'].append(sample['value'])

for k in data.keys():
    data[f'{k}']['temp'] = data[f'{k}']['temp'][44:]
    data[f'{k}']['humidity'] = data[f'{k}']['humidity'][43:]

# GET EVERY TWO POINTS
#print(data['Sensor 1']['temp'])
for k in data.keys():
    templist = []
    humlist = []
    for i in range(0,len(data[f'{k}']['temp'])):
        if i%2==0:
            #print(data[f'{k}']['temp'][i])
            templist.append(data[f'{k}']['temp'][i])
    for i in range(0, len(data[f'{k}']['humidity'])):
        if i % 2 == 0:
            humlist.append(data[f'{k}']['humidity'][i])
    data[f'{k}']['temp'] = templist
    data[f'{k}']['humidity'] = humlist

data["Sensor 1"]["temp"] = data["Sensor 1"]["temp"][1:]

for k in data.keys():
    data[f"{k}"]["temp"]=data[f"{k}"]["temp"][:576]
    data[f"{k}"]["humidity"]=data[f"{k}"]["humidity"][:576]

mean_temp = [(a+b+c+d) / 4 for a,b,c,d in zip(data["Sensor 1"]["temp"],data["Sensor 2"]["temp"],data["Sensor 3"]["temp"],data["Sensor 4"]["temp"])]
mean_hum = [(a+b+c+d) / 4 for a,b,c,d in zip(data["Sensor 1"]["humidity"],data["Sensor 2"]["humidity"],data["Sensor 3"]["humidity"],data["Sensor 4"]["humidity"])]

#-------PLOTS TEMPERATURE-------
#PREDICT


#----A. INDOOR VS OUTDOOR----
lbls = ['Dec/10/22 0:00','Dec/10/22 12:00','Dec/11/22 0:00','Dec/11/22 12:00','Dec/12/22 0:00']
# plt.subplot(2,1,1)
# plt.plot(mean_temp, label='Indoor', alpha = 0.7)
# plt.plot(temp, label='Outdoor')
# plt.title('Outdoor vs Indoor Average Temperature',fontsize=16.0, fontweight='bold')
# plt.yticks(range(12,27,2))
# plt.xticks(range(0,577,144), lbls)
# plt.ylabel('Temperature (°C)',fontsize=10.0, fontweight='bold')
# plt.xlabel('Date and Time',fontsize=10.0, fontweight='bold')
# plt.legend()
#
# plt.subplot(2,1,2)
# plt.plot(mean_hum, label='Indoor', alpha = 0.7)
# plt.plot(hum, label='Outdoor', alpha = 0.7)
# plt.title('Outdoor vs Indoor Average Humidity',fontsize=16.0, fontweight='bold')
# print(min(mean_hum))
# print(min(hum))
# print(max(mean_hum))
# print(max(hum))
# plt.yticks(range(20,63,6))
# plt.xticks(range(0,577,144), lbls)
# plt.ylabel('Humidity (%)',fontsize=10.0,fontweight='bold')
# plt.xlabel('Date and Time',fontsize=10.0, fontweight='bold')
plt.title('Outdoor Temperature')
x=np.arange(0,565)
plt.scatter(x,temp)
plt.ylabel('Temperature(°C)')
plt.xticks(range(0,577,144), lbls)


plt.legend()
plt.tight_layout()
plt.show()


#----B.