## Basic Class and Object
## Problem: Create a car class with attributes like brand and model. Then create an instance of this class.

class Car:
    brand = "Mahindra"
    model = "Thar"

my_car = Car()
print(my_car.brand)
print(my_car.model)

print(50*"#")

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

my_car = Car("Toyota", "Corolla")
print(my_car.brand)
print(my_car.model)

print(50*"#")

my_new_car= Car("TATA", "Safari")
print(my_new_car.brand)
print(my_new_car.model)