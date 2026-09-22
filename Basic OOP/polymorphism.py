class Car:
    def move(self):
        print("Driving")

class Plane:
    def move(self):
        print("Flying")

def start_journey(vehicle):
    vehicle.move()

car = Car()
plane = Plane()

start_journey(car)
start_journey(plane)