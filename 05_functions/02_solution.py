## Function with Multiple Parameters
## Problem: Create a function that takes two numbers as parameters and returns their sum.

def sum_of_two(num_one, num_two):
    return num_one+num_two

a = float(input("Give the first number: "))
b = float(input("Give the second number: "))
print("The sum is:", sum_of_two(a, b))