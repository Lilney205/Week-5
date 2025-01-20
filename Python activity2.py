class Vehicle:
    # Base class for vehicles
    def move(self):
        pass  # To be overridden in subclasses

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")


# Creating objects and calling move()
car = Car()
plane = Plane()
boat = Boat()

car.move()
plane.move()
boat.move()
