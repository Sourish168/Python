## Sum of Even Numbers
## Problem: Calculate the sum of even numbers upto a given number n.

n = int(input("Give the conditional number for stopping: "))
sum_even = 0

for i in range(1, n+1):
    if i%2==0:
        sum_even += i

print("Sum of even numbers is: ", sum_even)