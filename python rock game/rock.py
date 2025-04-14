import random


user_choice = None

options = ["rock", "paper", "scissors"]
computer_choice = random.choice(options)


while True:
    user_choice = input("Enter rock, paper, or scissors (or 'exit' to quit): ").lower()

    if user_choice == "exit":
        print("Goodbye!")
        break

    if user_choice not in options:
        print("Invalid choice. Please try again.")
        continue

    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")

    computer_choice = random.choice(options)
    
    