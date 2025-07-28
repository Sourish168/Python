username = "sourish_in_python"

# In other languages:
# function test(){
#     Body of the function in curly braces
# }

# In python:
# def test():
#     Body of the function in indentation
#     pass

print(20*"##")

def func():
    username = "sourish"
    print("This is the local scope:", username)

print("This is the global scope:", username)
func()

print(20*"##")

def func():
    # username = "sourish"
    print("This is the local scope:", username)

func()

print(20*"##")

x = 99
print("global x =", x)
def func2(y):
    z = x+y
    print("local y =", y)
    return z

print("global x + local y =", func2(1))

print(20*"##")

def func3():
    x = 88
    print("local x =", x)

func3()
print("global x =", x)

print(20*"##")

def func3():
    global x # Make the changes in global scope
    x = 77
    print("local x =", x)

func3()
print("global x =", x)

print(20*"##")

x = 99
print("global x =", x)
def f1():
    x = 88
    print("local_1 x =", x)
    def f2():
        x = 77
        print("local_2 x =", x)
        def f3():
            x = 66
            print("local_3 x =", x)
        f3()
    f2()
f1()

print(20*"##")

x = 99
print("global x =", x)
def f1():
    x = 88
    print("local_1 x =", x)
    def f2():
        x = 77
        print("local_2 x =", x)
        def f3():
            x = 66
            print("local_3 x =", x)
        return f3 # Closure
    return f2 # Closure
result = f1()
result()

print(20*"##")

def main(num):
    def sub1(x):
        def sub2(y):
            return (y*x)**num
        return sub2
    return sub1

k = main(2)
c = main(3)
print(k)
print(c)
print(k(2))
print(c(2))

l = k(2)
d = c(3)
print(l)
print(d)
print(l(3))
print(d(2))

print("(num, x, y) = (2, 3, 4) =>", main(2)(3)(4))