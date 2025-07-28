## Multiple Inheritance
## Problem: Create two classes Battery and Engine, and let the ElectricCar inherit from both, demonstrating multiple inheritance

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
    
    @staticmethod  # Decorators
    def general_description(): # Static method thus not accessed by instances only for class
        return "Cars are means of transport"
    
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


class Battery:
    def battery_info(self):
        return "This is the battery"

class Engine:
    def engine_info(self):
        return "This is the engine"

class ElectricCarTwo(Battery, Engine, Car): # Multiple Inheritance
    pass

my_new_car = ElectricCarTwo("Mahindra", "XUV 300")

print(my_new_car.engine_info())
print(my_new_car.battery_info())
print(isinstance(my_new_car, ElectricCarTwo))
print(isinstance(my_new_car, Battery))
print(isinstance(my_new_car, Engine))