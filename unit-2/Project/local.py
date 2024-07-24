import requests
from matplotlib import pyplot as plt
import warnings
warnings.simplefilter('ignore')
import numpy as np

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

#---------------PLOTS---------------
#--A. EACH ROOM--
#plt.subplot(2,1,1)
#plt.title("Room Sensor 4 - Temperature")
#plt.xticks(range(0,len(data["Sensor 4"]["temp"]),))
#plt.plot(data["Sensor 4"]["temp"])
#plt.subplot(2,1,2)
#plt.title("Room Sensor 4 - Humidity")
#plt.plot(data["Sensor 4"]["humidity"])

#--B. ALL SENSORS PLOT--
#for k in data.keys():
#    plt.plot(data[f"{k}"]["temp"],label=f"{k}",alpha=0.5)

#plt.title('Indoor Temperature (Data from 4 sensors)')
#plt.xticks(range(0,577,144), ['Dec 10',' ','Dec 11',' ','Dec 12'],rotation=20)
#plt.ylabel('Temperature (C)')
#plt.legend()
#plt.show()

#--C. MEAN, ROOM TEMP--
mean_temp = [(a+b+c+d) / 4 for a,b,c,d in zip(data["Sensor 1"]["temp"],data["Sensor 2"]["temp"],data["Sensor 3"]["temp"],data["Sensor 4"]["temp"])]
mean_hum = [(a+b+c+d) / 4 for a,b,c,d in zip(data["Sensor 1"]["humidity"],data["Sensor 2"]["humidity"],data["Sensor 3"]["humidity"],data["Sensor 4"]["humidity"])]
# median_temp = [np.median([a,b,c,d]) for a,b,c,d in zip(data["Sensor 1"]["humidity"],data["Sensor 2"]["humidity"],data["Sensor 3"]["humidity"],data["Sensor 4"]["humidity"])]
# mean_hum = [np.median([a,b,c,d]) for a,b,c,d in zip(data["Sensor 1"]["humidity"],data["Sensor 2"]["humidity"],data["Sensor 3"]["humidity"],data["Sensor 4"]["humidity"])]
# lbls = ['Dec/10/22 0:00','Dec/10/22 12:00','Dec/11/22 0:00','Dec/11/22 12:00','Dec/12/22 0:00']
#
# plt.plot(median_temp)
# plt.title('Median Temperature',fontsize=11.0, fontweight='bold')
# plt.xticks(range(0,577,144), lbls)
# plt.ylabel('Temperature (°C)',fontsize=10.0)
# plt.xlabel('Date and Time',fontsize=10.0)

#print(f'mean_temp=[{mean_temp}]\nmean_hum = [{mean_hum}]')
#plt.plot(mean_temp)

fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(18, 5))

fig = plt.figure(figsize = ([12,6]))
gs = gridspec.GridSpec(4,7)
gs.update(wspace=1.5,hspace=0.7)

ax1 = plt.subplot(gs[0:2,0:3])
ax1.set_ylabel('Humidity (%)', labelpad = 0, fontsize = 8)
ax1.plot(mean_hum)
ax1.title.set_text('Mean Humidity of 4 sensors')
ax1.set_xticks(range(0,577,144), ['Dec 10',' ','Dec 11',' ','Dec 12'])

ax2 = plt.subplot(gs[0,3:6])
ax2.set_ylabel('Humidity (%)', labelpad = 0, fontsize = 8)
ax2.plot(data["Sensor 1"]["humidity"])
ax2.set_xticks(range(0,577,144), ['Dec 10',' ','Dec 11',' ','Dec 12'])
ax2.title.set_text('Sensor 1 Humidity')

ax3 = plt.subplot(gs[1,3:6])
ax3.set_ylabel('Humidity (%)', labelpad = 0, fontsize = 8)
ax3.plot(data["Sensor 2"]["humidity"])
ax3.set_xticks(range(0,577,144), ['Dec 10',' ','Dec 11',' ','Dec 12'])
ax3.title.set_text('Sensor 2 Humidity')

ax4 = plt.subplot(gs[2,3:6])
ax4.set_ylabel('Humidity (%)', labelpad = 0, fontsize = 8)
ax4.plot(data["Sensor 3"]["humidity"])
ax4.set_xticks(range(0,577,144), ['Dec 10',' ','Dec 11',' ','Dec 12'])
ax4.title.set_text('Sensor 3 Humidity')

ax5 = plt.subplot(gs[3,3:6])
ax5.set_ylabel('Humidity (%)', labelpad = 0, fontsize = 8)
ax5.plot(data["Sensor 4"]["humidity"])
ax5.set_xticks(range(0,577,144), ['Dec 10',' ','Dec 11',' ','Dec 12'])
ax5.title.set_text('Sensor 4 Humidity')


ax6 = plt.subplot(gs[2:4,0:3])
ax6.set_ylabel('Humidity (%)', labelpad = 0, fontsize = 8)
ax6.title.set_text('Humidity of 4 sensors')
for k in data.keys():
    ax6.plot(data[f"{k}"]["humidity"],label=f"{k}",alpha=0.5)
ax6.set_xticks(range(0,577,144), ['Dec 10',' ','Dec 11',' ','Dec 12'])
#
plt.tight_layout()
plt.legend()
plt.show()


