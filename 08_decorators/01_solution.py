## Timing Function Execution
## Problem: Write a decorator that measures the time a function takes to execute

import time # Since we have to calculate the time, else not at all related to decorators

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        output = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} second time")
        return output
    return wrapper

@timer # Decorator, through which the underlying code should pass first
def example_function(n):
    time.sleep(n)

example_function(2)