## Function Returning Multiple Values
## Problem: Create a function that returns both the area and circumference of a circle given its radius

import math

def circle_info(radius):
    area = math.pi*(radius**2)
    circumference = 2*math.pi*radius
    return area, circumference

a = float(input("Give the radius of the circle: "))
b, c = circle_info(a)

print("The area of the circle is:", round(b, 3))
print("The circumference of the circle is:", round(c, 3))