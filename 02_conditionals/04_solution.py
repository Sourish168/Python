## Fruit Ripeness Checker
## Problem: Determine if a fruit is ripe, overripe, or unripe based on its color.(e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

fruit=str(input("Please enter your favorite fruit name: ")).lower()
color=str(input("Please mention the color of the fruit: ")).lower()

if fruit=="banana":
    condition="overripe" if color=="brown" else "ripe" if color=="yellow" else "green" if color=="green" else -1
else:
    print(f"The {fruit} information is not available")
    exit()

if condition==-1:
    print(f"Please enter a valid color of {fruit}")
else:
    print(f"The {fruit} is in {condition} condition")