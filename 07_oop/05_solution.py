## Polymorphism
## Problem: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

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

print(50*"#")

safari = Car("Tata", "Safari")
print(safari.fuel_type())