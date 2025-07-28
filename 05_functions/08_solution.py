## Function with **kwargs
## Problem: Create a function that accepts any number of keyword arguments and print them in the format key:value

# def print_kwargs(name, weapon, time):  # The problem arises when we don't know which *args is going to where, so *args is not an option, thus **kwargs importances comes
#     print("Name:", name, "Weapon:", weapon, "Time:", time)

def print_kwargs(**kwargs):  # **kwargs takes key, value pairs
    # print(*kwargs)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="Ram", weapon="Bow", time="Treta")
print_kwargs(name="Ram")
print_kwargs(name="Ram", friend="Hanuman", time="Treta")
# print_kwargs(name="Ram", name="Ram", friend="Hanuman", time="Treta")  # Gives error since for same key name there are 2 values Ram and Lakshman