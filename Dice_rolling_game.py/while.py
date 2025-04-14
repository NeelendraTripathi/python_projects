import random
fruits = ["apple", "banana", "cherry"]
attempt = 6
print("You have 6 attempt match the fruit: ")
num=input("Enter the any fruit please: ")
for x in fruits:
    if x==num:
        print(f"The fruit is match: {x}")
        break
    else:
        print("invalid input:")

