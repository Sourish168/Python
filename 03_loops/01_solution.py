## Counting Positive Numbers
## Problem: Given a list of numbers, count how many are positive
## numbers = [1, 2, 3, -2, -1, 6, 5, -11, -4, 4, -10, 9, -9, -6, 8, 7]
 
numbers = [1, 2, 3, -2, -1, 6, 5, -11, -4, 4, -10, 9, -9, -6, 8, 7]

pos_num_count = 0
for num in numbers:
    if num > 0:
        pos_num_count += 1
print("Total count of positive number is: ", pos_num_count)