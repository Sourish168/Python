## Default Parameter Value
## Problem: Write a function that greets a user. If no name is provided, it should greet with a default name

def greetings(name="Sourish"):
    return f"Hi {name}, Nice to meet you!!! \nHave a nice day dear..."

print(greetings("Python"))
print(greetings())