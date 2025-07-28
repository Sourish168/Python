## Class Inheritance and isinstance() Function
## Problem: Demonstrate the use of isinstance() to check if my_tesla ia an instance of Car and ElectricCar

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

# print(Car.total_car) # Considering the child class also (e.g. ElectricCar)

print(50*"#")

print(isinstance(my_tesla, Car))
print(isinstance(my_tesla, ElectricCar))

print(50*"#")

print(isinstance(safari, Car))
print(isinstance(safari, ElectricCar)) # Since safari is not an instance of ElectricCar