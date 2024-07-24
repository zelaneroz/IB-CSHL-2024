from matplotlib import pyplot as plt
import requests
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

#---------------
#fig = plt.figure(figsize=(10,8))
#spec = fig.add_gridspec(4,4)

#def annotate_axes(ax,data):
#    ax.plot(data)

mean_temp = []
mean_hum = []
# ACCESS EVERY KEY["TEMPERATURE"] FROM THE DICTIONARY
# FOR K IN DICTIONARY.KEYS
# ADD EACH DATA FOR EACH OTHER AND DIVIDE BY 4
# APPEND THE ABOVE TO MEAN_TEMP OR MEAN_HUM



#x0 = fig.add_subplot(spec[:,0:2])
#annotate_axes(ax0,res) #CHANGE TO MEAN

#plt.title
#plt.tight_layout()
#plt.show()