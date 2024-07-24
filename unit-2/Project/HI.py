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
def smoothing(data,window):
    data_ma_mph = []
    data_ma_sth = []
    for t in range(0,len(data),window):
        t_hour = data[t:t+window]
        data_ma_mph.append(sum(t_hour) / len(t_hour))
        data_ma_sth.append(np.std(t_hour))
    return data_ma_mph, data_ma_sth
window=12

#----A. INDOOR VS OUTDOOR----
lbls = ['Dec/10/22 0:00','Dec/10/22 12:00','Dec/11/22 0:00','Dec/11/22 12:00','Dec/12/22 0:00']

#f = plt.figure()
#f.set_figheight(15)
#f.set_figwidth(15)
def max_min(temp1,temp2,temp3,temp4):
    max_in_temp, min_in_temp = [], []
    for i in range(len(temp1)):
        max_in_temp.append(max([temp1[i],temp2[i],temp3[i],temp4[i]]))
        min_in_temp.append(min([temp1[i], temp2[i], temp3[i], temp4[i]]))
    return max_in_temp, min_in_temp

y1,y2 = max_min(smoothing(data['Sensor 1']['temp'],window),smoothing(data['Sensor 2']['temp'],window),smoothing(data['Sensor 3']['temp'],window),smoothing(data['Sensor 4']['temp'],window))
print(y1, '\n\n',y2)
x=np.arange(len(smoothing(mean_temp,window)[0]))
plt.plot(x, smoothing(mean_temp,window)[0])
plt.title('Smoothed Indoor Average Temperature',fontsize=12.0, fontweight='bold')
plt.yticks(range(13,28,2))
plt.xticks(range(0,len(smoothing(hum,window)[0])+1,12),lbls)
plt.ylabel('Temperature (°C)',fontsize=10.0)
plt.xlabel('Date and Time',fontsize=10.0)
y=smoothing(mean_temp,window)[0]
plt.fill_between(x,y1[0],y2[0],alpha=0.4,linewidth=0, color='#8ecae6')
plt.errorbar(x,y,yerr=np.std(y),fmt='o')


# plt.subplot(4,2,1)
# plt.plot(mean_temp)
# plt.title('Indoor Average Temperature',fontsize=12.0, fontweight='bold')
# plt.yticks(range(13,28,2))
# plt.xticks(range(0,577,144), lbls)
# plt.ylabel('Temperature (°C)',fontsize=10.0)
# plt.xlabel('Date and Time',fontsize=10.0)
#
# plt.subplot(4,2,2)
# plt.plot(np.arange(len(smoothing(mean_temp,window)[0])), smoothing(mean_temp,window)[0])
# plt.title('Smoothed Indoor Average Temperature',fontsize=12.0, fontweight='bold')
# plt.yticks(range(13,28,2))
# plt.xticks(range(0,len(smoothing(hum,window)[0])+1,12),lbls)
# plt.ylabel('Temperature (°C)',fontsize=10.0)
# plt.xlabel('Date and Time',fontsize=10.0)
#
# plt.subplot(4,2,3)
# plt.title('Outdoor Temperature',fontsize=12.0, fontweight='bold')
# plt.plot(temp)
# plt.yticks(range(13,28,2))
# plt.xticks(range(0,577,144), lbls)
# plt.ylabel('Temperature (°C)',fontsize=10.0)
# plt.xlabel('Date and Time',fontsize=10.0)
#
#
# plt.subplot(4,2,4)
# plt.title('Smoothed Outdoor Temperature',fontsize=12.0, fontweight='bold')
# plt.plot(np.arange(len(smoothing(temp,window)[0])), smoothing(temp,window)[0])
# plt.yticks(range(13,28,2))
# plt.xticks(range(0,len(smoothing(hum,window)[0])+1,12),lbls)
# plt.ylabel('Temperature (°C)',fontsize=10.0)
# plt.xlabel('Date and Time',fontsize=10.0)
#
#
# plt.subplot(4,2,5)
# plt.plot(mean_hum)
# plt.title('Indoor Average Humidity',fontsize=12.0, fontweight='bold')
# plt.yticks(range(20,63,6))
# plt.xticks(range(0,577,144), lbls)
# plt.ylabel('Humidity (%)',fontsize=10.0)
# plt.xlabel('Date and Time',fontsize=10.0)
#
#
# plt.subplot(4,2,6)
# plt.plot(np.arange(len(smoothing(mean_hum,window)[0])), smoothing(mean_hum,window)[0])
# plt.title('Smoothed Indoor Average Humidity',fontsize=12.0, fontweight='bold')
# plt.yticks(range(20,63,6))
# plt.xticks(range(0,len(smoothing(hum,window)[0])+1,12),lbls)
# plt.ylabel('Humidity (%)',fontsize=10.0)
# plt.xlabel('Date and Time',fontsize=10.0)
#
#
# plt.subplot(4,2,7)
# plt.plot(hum)
# plt.title('Outdoor Humidity',fontsize=12.0, fontweight='bold')
# plt.yticks(range(20,63,6))
# plt.xticks(range(0,577,144), lbls)
# plt.ylabel('Humidity (%)',fontsize=10.0)
# plt.xlabel('Date and Time',fontsize=10.0)
#
#
# plt.subplot(4,2,8)
# plt.plot(np.arange(len(smoothing(hum,window)[0])), smoothing(hum,window)[0])
# plt.title('Smoothed Outdoor Humidity',fontsize=12.0, fontweight='bold')
# plt.yticks(range(20,63,6))
# plt.xticks(range(0,len(smoothing(hum,window)[0])+1,12),lbls)
# plt.ylabel('Humidity (%)',fontsize=10.0)
# plt.xlabel('Date and Time',fontsize=10.0)


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
plt.savefig('all.png')
plt.tight_layout()
plt.show()

print(f'temp: , max({max(temp)}),min({min(temp)})')
print(f'mean_temp: , max({max(mean_temp)}),min({min(mean_temp)})')
print(f'temp: , max({max(hum)}),min({min(hum)})')
print(f'mean_temp: , max({max(mean_hum)}),min({min(mean_hum)})')
