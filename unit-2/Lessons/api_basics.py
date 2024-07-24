import requests
import random
from matplotlib import pyplot as plt
import warnings
warnings.simplefilter('ignore')
response = requests.get("http://192.168.6.142/readings")
print(response.status_code)
print(response.json())
#200 - Everything went okay, and the result has been returned (if any)

#DICTIONARIES
sensor={"name":"sensor_x1","type":"Temperature","readings":[]}
print(sensor["type"])
sensor["samples"]=[]
for i in range(10):
    sensor["readings"].append(random.randint(1,200))
    sensor["samples"].append(i)


data={
    "type": "temperature",
    "id": 1,
    "unit": "celcius",
    "name": "sensor_x1",
    "readings": [
        {
            "value": 23.022,
            "sensor_id": 1,
            "id": 1,
            "datetime": "2021-11-25T21:34:50.027731"
        },
        {
            "value": 23.022,
            "sensor_id": 1,
            "id": 2,
            "datetime": "2021-11-29T19:32:10.363180"
        }]
}

x,y = [],[]
sample = 0
readings = data["readings"]
for r in readings:
    print(r["value"],r["datetime"])
    y.append(r["value"])
    x.append(sample)
    sample+=1


print(sensor)
plt.plot(sensor["samples"],sensor["readings"])
plt.show()

