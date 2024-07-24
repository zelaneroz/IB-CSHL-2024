import matplotlib.pyplot as plt
import requests
from matplotlib import pyplot as plt
import warnings
import numpy as np
warnings.simplefilter('ignore')

response = requests.get("http://192.168.6.142/readings")
data = response.json()
readings = data['readings'][0]


#SENSOR_ID = 1 FOR TEMP | SENSOR_ID = 2 FOR HUMIDITY
hum = []
for sample in readings:
    if sample['sensor_id']==2:
        hum.append(sample['value'])

plt.plot(hum)
plt.show()