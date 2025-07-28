## Pet Food Recommedention
## Problem: Recommend a type of pet food based on te pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food)

pet=str(input("Mention the pet you have: ")).lower()
age=float(input(f"Please mention the age of your {pet} in years: "))

if pet=="dog":
    if age<2:
        print(f"The best food for your {pet} is puppy food")
    else:
        print(f"The best food for your {pet} is doggy food")
elif pet=="cat":
    if age>5:
        print(f"The best food for your {pet} is senior cat food")
    else:
        print(f"The best food for your {pet} is junior cat food")
else:
    print(f"The required food for your {pet} is not available")