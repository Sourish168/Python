## Property Decorators
## Problem: Use a property decorator in the Car class to make the model attribute read-only

class Car:
    total_car = 0 # Definig new variable to get the count

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model # _Underscore makes the property private i.e. hides the variable that cannot be overwritten
        Car.total_car += 1 # Method 1 to get the count

    def get_brand(self):
        return self.__brand + " !"
    
    def set_brand(self, brand):
        self.__brand = brand
    
    def full_name(self):
        return f"{self.__brand}: {self.__model}"
    
    def fuel_type(self): # Same function but different operations(Return)
        return "Petrol or Diesel"
    
    @staticmethod  # Decorators
    def general_description(): # Static method thus not accessed by instances only for class
        return "Cars are means of transport"
    
    @property # This makes sure that we cannot update the __model variable, also useful to read-only mode and other decorated outputs
    def model(self):
        return self.__model

safari = Car("Tata", "Safari")
print(safari.model)
print(safari.full_name())

print(50*"#")

safari.model = "Manza"
print(safari.model)
print(safari.full_name())
