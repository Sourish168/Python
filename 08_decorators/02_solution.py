## Debugging Function Calls
## Problem: Create a decorator to print the function name and the values of its arguments every time the function is called

def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ", ".join(str(arg) for arg in args)
        kwarg_value = ", ".join(f"{k}: {v}" for k, v in kwargs.items())
        print(f"Calling: {func.__name__} \nargs \n{args_value} \nkwargs \n{kwarg_value}")
        return func(*args, **kwargs)
    return wrapper

@debug
def greet(name, greeting="Hi"):
    print(f"{greeting}, {name}")

@debug
def hello():
    print("Hello!")

hello()
greet(greeting="Dear", name="Sourish")