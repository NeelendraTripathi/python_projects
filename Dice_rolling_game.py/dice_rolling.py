import random
i=0
choice =input("Roll the choice(Y/N)? ").lower()

if choice =='y':
    die1=random.randint(1,6)
    die2=random.randint(1,6)
    print(f"{die1},{die2}")
elif choice =='n':
    print("Thank you for playing!")
else:
    print("Invalid choice:")
for i in die1:
    print(f"The dice roll{i}")
    i+=1