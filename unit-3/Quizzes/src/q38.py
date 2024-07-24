import random
from matplotlib import pyplot as plt
from Lessons.main import city, coordinate,country

jp_cities=['Tokyo','Yokohama','Osaka',' Nagoya','Sapporo','Kobe','Kyoto','Fukuoka','Kawasaki','Saitama']

japan = country(name="Japan")
for ct in jp_cities:
    x_rand = random.randint(0,100)
    y_rand = random.randint(0,100)
    ct = city(name=ct,location=coordinate(x_rand,y_rand))
    japan.add_city(city_to_add=ct)

for i in japan.cities:
    x=i.location.x
    y=i.location.y
    plt.text(x,y,i.name)
    plt.scatter(x,y,s=100)
plt.xlabel("Distance(km)")
plt.ylabel("Distance(km)")
plt.savefig('q38.png')
plt.show()