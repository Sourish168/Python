## Function with *args
## Problem: Write a function that takes variable number of arguments and returns their sum

def sum_all(*args): # For taking any number of parameters in a function we use *args
    a = 0
    # print(*args)
    for i in args:
        a += i
    return a

print(sum_all(1, 2, 3, 4))
print(sum_all(1, 3, 5, 7, 9, 11))
print(sum_all(2, 6, 10, 14, 18, 24, 28, 32))