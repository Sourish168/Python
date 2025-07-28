## List Uniqueness Checker
## Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate

items = ["apple", "banana", "orange", "apple", "mango"]
unique_item = set()

for item in items:
    if item in unique_item:
        print("The duplicate in the list is:", item)
        break
    unique_item.add(item)