## Transportation Mode Selection
## Problem: Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car)

distance = float(input("Write the distance in Kms between beginning and destination points: "))

medium = "walk" if distance<3 else "bike" if distance<=15 else "car"

print(f"So, you should travel by {medium} according to the distance")