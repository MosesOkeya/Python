Activity 1: Superhero Class with Inheritance and Encapsulation

# Base class
class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self._power = power  # Protected attribute
        self.origin = origin

    def show_identity(self):
        print(f"I am {self.name}, from {self.origin}!")

    def use_power(self):
        print(f"{self.name} uses {self._power}!")

# Subclass - inherits from Superhero
class Speedster(Superhero):
    def __init__(self, name, origin, top_speed):
        super().__init__(name, "Super Speed", origin)
        self.top_speed = top_speed

    def use_power(self):
        print(f"{self.name} runs at lightning speed: {self.top_speed} km/h!")

# Subclass - inherits from Superhero
class Flyer(Superhero):
    def __init__(self, name, origin, altitude_limit):
        super().__init__(name, "Flight", origin)
        self.altitude_limit = altitude_limit

    def use_power(self):
        print(f"{self.name} soars up to {self.altitude_limit} meters!")

# Example usage
hero1 = Speedster("Flashburn", "Metro City", 1000)
hero2 = Flyer("SkyBlade", "Skyhold", 10000)

hero1.show_identity()
hero1.use_power()

hero2.show_identity()
hero2.use_power()


---

Activity 2: Polymorphism Challenge (Vehicles)

class Vehicle:
    def move(self):
        print("Vehicle is moving...")

class Car(Vehicle):
    def move(self):
        print("Driving on the road! 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying in the sky! ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing on the water! 🚤")

# Demonstrating polymorphism
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()


