## Generator Function with yield
## Problem: Write a generator function that yields even numbers up to a specified limit

lim = int(input("Write a number for generating even numbers: "))

def even_generator(limit):
    for i in range(2, limit+1, 2):
        yield i  # yield makes a generator object that is iterable and doesn't end the function like return

for num in even_generator(lim):
    print(num)