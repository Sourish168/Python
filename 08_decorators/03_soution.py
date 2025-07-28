## Cache Return Values
## Problem: Implement a decorator that caches the return values of a function, so that when it's called with the same arguments, the cached value is returned instade of re-executing the function

import time

def cache(func):
    cache_value = {}
    print(cache_value)
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        output = func(*args)
        cache_value[args] = output
        return output
    return wrapper

@cache
def long_running_function(a, b):
    time.sleep(4)
    return a+b


print(long_running_function(2, 3))
print(long_running_function(2, 3))
print(long_running_function(3, 3))
print(long_running_function(2, 2))