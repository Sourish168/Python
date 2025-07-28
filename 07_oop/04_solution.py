## Encapsulation
## Problem: Modify the Car class to encapsulate the brand attribute, making it private and provide a getter method for it

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
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

my_tesla = ElectricCar("Tesla", "Model S", "87kWh")

print(my_tesla.full_name())
# print(my_tesla.__brand) # Gives error, for unable to access the brand
print(my_tesla.get_brand())

print(my_tesla.set_brand("Tesla V2"))
print(my_tesla.get_brand())
print(my_tesla.full_name())