## Multiplication Table Printer
## Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration

number = int(input("Give a number to print the multiplication table: "))
k = int(input("Enter the number you want to skip: "))

for i in range(1, 11):
    if i!=k:
        print(f"{number} X {i} = {number*i}")
    else:
        # print(f"{i} is skipped!!!")
        continue