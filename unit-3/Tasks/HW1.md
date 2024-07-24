# Homework 1

## Given Code
```.py
class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"[Coordinate class]: x={self.x} y={self.y}"

class City:
    def __init__(self, name:str, location:Coordinate):
        self.name = name
        self.location = location

    def __repr__(self) -> str:
        return f"[City class] {self.name} located at {self.location}"

    def get_name(self):
        return self.name

    def get_location(self,CityB):
         self.location.x


class Country:
    def __init__(self, name) -> None:
        self.city_list = []
        self.name = name

    def __repr__(self) -> str:
        return f"[Country Class] {self.name} with cities: {self.city_list}"

    def add_city(self, city_to_add:City):
        if isinstance(city_to_add, City):
            self.city_list.append(city_to_add)
        else:
            raise ValueError("City must be a City Object")

    def remove_city(self, city_to_remove:City):
        self.city_list = [value for value in self.students if value != city_to_remove]

```

## (1) Create 10 random cities in a unit 3 smart way
```.py
cities_data = [
    ["Tokyo", Coordinate(1,3)],
    ["Shibuya", Coordinate(2,1)],
    ["Shinjuku", Coordinate(3,3)],
    ["Nagoya", Coordinate(4,4)],
    ["Kobe", Coordinate(5,6)],
    ["Osaka", Coordinate(6,7)],
    ["Fukuoka", Coordinate(7,12)],
    ["Hiroshima", Coordinate(9,21)],
    ["Okinawa", Coordinate(12,12)],
    ["Sapporo", Coordinate(17,12)],
]

Japan = Country(name="Japan")

for i in cities_data:
  new_city = City(i[0], i[1])
  Japan.add_city(city_to_add=new_city)
```

## (2) Create a method in the class city 
This class receives as input another city & return the distance between the two cities

Distance Formula:
$d= \sqrt{(y_2-y_1)^2+(x_2-x_1)^2}$

```.py
class city:
...
  def distance(self, ct2):
    x1,y1=self.location.x,self.location.y
    x2,y2=ct2.location.x,ct2.location.y
    dist=((x1-x2)**2+(y1-y2)**2)**(1/2)
    return round(dist,3)
```

## (3) What is the salesman problem? Existing solutions?
*500 characters*

**The Problem**
The Traveling Salesman Problem (TSP) tries to find the best route to visit a certain set of places and come back to the starting point. Like a salesman, you need to visit cities to sell products, but you want to do it the most efficient way possible - shortest distance & visit each city once. It's important to note that in TSP, the higher the number of "cities" to get to, the harder it gets. Given its nature, the TSP is often used for optimizing algorithms and problems like package delivery etc.
*Character Count: 500*

**The Solution**
* Brute Force: Try all possible routes and then choose the shortest; this becomes unfeasible as the number of cities increases.
* Approximation Algorithms: Provides a solution close to the optimal solution, but not really the shortest.
* Optimization Algorithms: Use mathematical formulas and computer algorithms to find the shortest route (ex. Branch & Bound method)
* Nearest Neighbor: Choose a random city then go for the closest unvisited city. Once all cities have been visited, return to the first one.  

*Character Count: 500*


