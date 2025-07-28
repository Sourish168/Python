## Polymorphism in Functions
## Problem: Write a finction multiply that multiplies two numbers, but can also accept and multipy strings

def multiply(first_num, second_num):
    return first_num * second_num

# a = input("Write first number/string to multipy: ")
# b = input("Write second number/string to multipy: ")

print("The multiplication is:", multiply(5, 6))
print("The multiplication is:", multiply(5, "b"))
print("The multiplication is:", multiply("b", 5))