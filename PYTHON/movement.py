
class Vehicle:
    def move(self):
        self.vehicle.move()
        
class Car(Vehicle):
    def move(self):
        print("🚗 The car is driving.")

class Plane(Vehicle):
    def move(self):
        print("✈️ The plane is flying.")

class Boat(Vehicle):
    def move(self):
        print("🚢 The boat is sailing.")

# Polymorphism in action
def travel(vehicle):
    vehicle.move()

# Example usage
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    travel(v)
