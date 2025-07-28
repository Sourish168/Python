## Lambda Function
## Problem: Create a lambda function to compute the cube of a number

num = float(input("Write a number: "))
cube = lambda x: x**3

print("The cube of the provided number is:", cube(num))