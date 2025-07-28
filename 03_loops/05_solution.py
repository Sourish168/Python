## Find the First Non-Repeated Character
## Problem: Given a string, find the first non-repeated character

input_str = str(input("Give a string for checking: "))

for char in input_str:
    if input_str.count(char)==1:
        print(f"The first non-repeated charecter is: {char}")
        break