## Movie Ticket Pricing
## Problem: Movie tickets are piced based on age: $12 for adults(18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.

age = int(input("Please write the age of the customer: "))
day = str(input("Please mention the weekday for the movie: ")).lower()

price = 12 if age>=18 else 8
discount = 2 if day=="wednesday" else 0

print(f"The price of the ticket is ${price - discount}")