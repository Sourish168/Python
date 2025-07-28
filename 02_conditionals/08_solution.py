## Password Strength Checker
## Problem: Check if a password is "Weak", "Medium", "Strong". Criteria: <6 chars(Weak), 6-10 chars(Medium), >10 chars(Strong)

password=str(input("Write your password: ")).lower()
strength = "weak" if len(password)<6 else "medium" if len(password)<=10 else "strong"

print(f"The strength of your password is {strength}")