## Coffee Customization
## Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra Shot" of espresso.

coffee_size = str(input("Choose the size of the coffee(Small/Medium/Large): ")).lower()
extra_shot = str(input("Need an extra shot(Yes/No): ")).lower()

if extra_shot=="yes":
    coffee = coffee_size + " coffee with an extra shot"
else:
    coffee = coffee_size + " coffee"

print(f"Your order is: {coffee}")