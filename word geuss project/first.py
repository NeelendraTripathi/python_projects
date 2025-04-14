# mini projects in guess the fruits
import random
print("!-------------------!>! Guess the fruit name !<!------------------!")
fruits =["apple", "banana", "cherry", "fig", "grape"]
print("You have 6 attempt guess the fruit:")

attemp = 6
def random_fruits_choice():
    random_fruit = random.choice(fruits)  
    return random_fruit
    print(f"Computer choice:{random_fruit}")
cmp = random_fruits_choice()

while attemp>0:
    user_choice=input("Guess the fruits name: ")
    if user_choice == cmp:
        print("You guessed the fruit:")
        break
    elif user_choice or not  fruits:
        print("Please input valid !")
        attemp-=1
        print(f"you are not guess fruit:,you have attempt: {attemp} ")
    if user_choice== 0:
        print("You are lose the chance: ")
    
        
    

    