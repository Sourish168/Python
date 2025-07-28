## Class Variable
## Problem: Add a class variable to Car that keeps track of the number of cars created

class Car:
    total_car = 0 # Definig new variable to get the count

    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_car += 1 # Method 1 to get the count

    def get_brand(self):
        return self.__brand + " !"
    
    def set_brand(self, brand):
        self.__brand = brand
    
    def full_name(self):
        return f"{self.__brand}: {self.model}"
    
    def fuel_type(self): # Same function but different operations(Return)
        return "Petrol or Diesel"
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self): # Same function but different operations(Return)
        return "Electric charge"

my_tesla = ElectricCar("Tesla", "Model S", "87kWh")
print(my_tesla.fuel_type())

safari = Car("Tata", "Safari")
print(safari.fuel_type())

print(Car.total_car) # Considering the child class also (e.g. ElectricCar)

print(50*"#")

thar = Car("Mahindra", "Thar Roxx")
print(thar.fuel_type())

print(thar.total_car)
print(safari.total_car)
print(Car.total_car)