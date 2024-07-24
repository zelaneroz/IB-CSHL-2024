class coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"[Coordinate Object]: x={self.x} y={self.y}"

class city:
    def __init__(self, name:str, location:coordinate):
        self.name = name
        self.location = location

    def __repr__(self) -> str:
        return f"[City Object] {self.name} located at {self.location}"

    def get_name(self):
        return self.name

    def get_location(self,CityB):
         self.location.x

    def distance(self, cityB):
        xa,ya = self.location.x, self.location.y
        xb,yb = cityB.location.x, cityB.location.y
        d=((xa-xb)**2 +(ya-yb)**2)**(1/2)
        return round(d,2)


class country:
    def __init__(self, name) -> None:
        self.cities = []
        self.name = name

    def __repr__(self) -> str:
        return f"[Country Class] {self.name} with cities: {self.cities}"

    def add_city(self, city_to_add:city):
        if isinstance(city_to_add, city):
            self.cities.append(city_to_add)
        else:
            raise ValueError("City must be a City Object")

    def remove_city(self, city_to_remove:city):
        self.cities = [value for value in self.students if value != city_to_remove]



cities_data = [
    ["Tokyo", coordinate(1,3)],
    ["Yokohoma", coordinate(2,1)],
    ["Osaka", coordinate(3,3)],
    ["Nagoya", coordinate(4,4)],
    ["Sapporo", coordinate(5,6)],
    ["Kobe", coordinate(6,7)],
    ["Kyoto", coordinate(7,12)],
    ["Fukuoka", coordinate(9,21)],
    ["Kawasaki", coordinate(12,12)],
    ["Saitama", coordinate(17,12)],
]

Japan = country(name="Japan")

for i in cities_data:
    new_city = city(i[0], i[1])
    Japan.add_city(city_to_add=new_city)

#print(Japan.cities[0].location.x)
#Dis
print(Japan.cities[6].distance(Japan.cities[9]))
