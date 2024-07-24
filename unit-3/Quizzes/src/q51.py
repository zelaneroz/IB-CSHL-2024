class Wheel:
    def __init__(self,wheel_size:int):
        self.size = wheel_size*2.54
    def get_size(self):
        return f"{self.size} cm"
    def get_perimeter(self):
        return f"Perimeter: {round(self.size*3.1415)}cm"
    def get_km_per_rotation(self):
        #rotations it takes per kilometers
        return f"It takes about {round(100000/(self.size*3.1415))} rotations to cover 1km."

    pass
class Bicycle:
    def __init__(self,size:int,frame_material):
        self.material =frame_material
        self.wheel = Wheel(size)
    def ride(self):
        return f"Bicycle Wheel Size: {self.wheel.size}\nBicycle Wheel Material: {self.material}"
        #print wheel size & frame material

test=Bicycle(26,'aluminum')
print(test.ride())
print(test.wheel.get_km_per_rotation())