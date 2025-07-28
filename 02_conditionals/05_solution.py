## Weather Activity Suggestion
## Problem: Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).

weather=str(input("Please mention your favorable weather: ")).lower()

if weather=="sunny":
    print(f"Go for a walk in this {weather} weather")
elif weather=="rainy":
    print(f"Read a book in this {weather} weather")
elif weather=="snowy":
    print(f"Build a snowman in this {weather} weather")
else:
    print(f"This {weather} weather information is not available")