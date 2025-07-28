## Recursive Function
## Problem: Create a recursive function to calculate the factorial of a number

num = int(input("Write a number to find factorial: "))

def factorial(n):
    if n == 0:
        return 1
    elif n < 0:
        return "Factorial of negative number does not exist."
    else:
        return n*factorial(n-1)
    
print(factorial(num))