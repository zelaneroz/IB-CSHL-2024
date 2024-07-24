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
        if i['datetime'][8:10] =='09' and i['datetime'][11:13] == '22':
            sample2.append(i['value'])
        elif i['datetime'][8:10] in ['10','11']:
            sample2.append(i['value'])
    #END_TIME
    #elif i['datetime'][8:10] =='11' and int(i['datetime'][11:13]) in range(0,22) and int(i['datetime'][14:16]) in range(0,36):
    #    sample2.append(i)
    return sample2

hum = times(hum)
temp = times(temp)
#fig = plt.figure((5,7))

#MOVING AVERAGE SMOOTHING
window=12 #WINDOW IS 12 SO THAT EVERY POINT IS A SUMMARY OF THE TEMP & HUMIDITY PER HOUR
def smoothing(data,window):
    data_ma_mph = []
    data_ma_sth = []
    for t in range(0,len(data),window):
        t_hour = data[t:t+window]
        data_ma_mph.append(sum(t_hour) / len(t_hour))
        data_ma_sth.append(np.std(t_hour))
    return data_ma_mph, data_ma_sth

x = np.arange(0,len(temp)+1,4)

# print(len(hum))
# print(len(smoothing(hum,window)[0]))
# plt.plot(hum)
# plt.title('Humidity')
# plt.ylabel('Humidity')
# plt.xticks(range(0,len(hum)+12,144), range(0,49,12))
# plt.xlabel('Hours since Dec 9, 9:35pm')
#
lbls = ['Dec 10',' ','Dec 11',' ','Dec 12']
plt.subplot(2,2,1)
plt.plot(hum)
plt.title('Humidity')
plt.ylabel('Humidity (%)')
plt.xticks(range(0,577,144), lbls)

plt.subplot(2,2,2)
plt.title('Humidity Data Smoothed')
plt.plot(np.arange(len(smoothing(hum,window)[0])), smoothing(hum,window)[0])
plt.xticks(range(0,len(smoothing(hum,window)[0])+1,12),lbls)
plt.ylabel('Humidity (%)')

plt.subplot(2,2,3)
plt.plot(temp)
plt.title('Temperature')
plt.ylabel('Temperature (C)')
plt.xticks(range(0,577,144), lbls)

plt.subplot(2,2,4)
plt.title('Temperature Data Smoothed')
plt.ylabel('Temperature (C)')
plt.plot(np.arange(len(smoothing(temp,window)[0])), smoothing(temp,window)[0])
plt.xticks(range(0,len(smoothing(hum,window)[0])+1,12),lbls)

# plt.subplot(3,2,5)
# plt.plot(temp, label='Humidity')
# plt.plot(hum, label='Temperature')
# plt.xticks(range(0,len(hum)+12,144), range(0,49,12))
# plt.legend()
#
# plt.subplot(3,2,6)
# counts,bins = np.histogram(hum)
# plt.stairs(counts,bins,label="Humidity")
# counts,bins = np.histogram(temp)
# plt.stairs(counts,bins,label="Temperature")
# plt.title('Temperature & Humidity Histogram')
# plt.xticks(range(0,len(smoothing(hum,window)[0])+1,12))

# plt.plot(temp, label='Humidity')
# plt.plot(hum, label='Temperature')
# plt.title("Outdoor Humidity & Temperature")
# plt.xticks(range(0,len(hum)+12,144), range(0,49,12))
# plt.xlabel('Hours since Dec 9, 10pm')

# counts,bins = np.histogram(hum)
# plt.stairs(counts,bins,label="Humidity")
# counts,bins = np.histogram(temp)
# plt.stairs(counts,bins,label="Temperature")
# plt.title('Temperature & Humidity Histogram')
# plt.xticks(range(0,len(smoothing(hum,window)[0])+1,12))


# plt.plot(hum)
# plt.title('Humidity')
# plt.ylabel('Humidity (%)')
# plt.xticks(range(0,len(hum)+12,144), range(0,49,12))
# plt.xlabel('Hours since Dec 9, 10pm')

#--------------------PLOT TEMP & HUM MAX & MIN
# plt.plot(temp)
# print(max(temp))
# print(min(temp))
# plt.title("Outdoor Temperature")
# plt.hlines(y=max(temp), label="Maximum", xmin=0,xmax=565, colors='darkorange')
# plt.hlines(y=min(temp), label="Minimum", xmin=0,xmax=565, colors='lime')
# plt.xticks(range(0,len(temp)+12,144), range(0,49,12))
# plt.yticks(range(13,max(temp)+1,2))
# plt.ylabel('Temperature (C)')
# plt.xlabel('Hours After Dec 9, 2022 10pm')
# plt.legend(loc='center left')

plt.xticks(range(0,577,144), ['Dec 10',' ','Dec 11',' ','Dec 12'])
plt.tight_layout()
plt.show()