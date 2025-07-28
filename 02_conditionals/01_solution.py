## Age Group Categorization
## Problem: Classify a person's age group: Child(<13), Teenager(13-19), Adult(20-59), Senior(60+)

age = int(input("Provide me a age: "))

if age<13:
    print("The user is a Child")
elif age<20:
    print("The user is a Teenager")
elif age<60:
    print("The user is a Adult")
else:
    print("The user is a Senior")