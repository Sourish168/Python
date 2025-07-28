## Grade Calculator
## Problem: Assign a letter grade based on a student's score: A(90-100), B(80-89), C(70-79), D(60-69), F(Below 60)

score = float(input("Please enter your score: "))

if score>100:
    print("Please verify your score again. That should be within the range of 0 to 100.")
    exit()

if score<60:
    grade="F"
elif score<70:
    grade="D"
elif score<80:
    grade="C"
elif score<90:
    grade="B"
else:
    grade="A"

print(f"You got a {grade} grade.")