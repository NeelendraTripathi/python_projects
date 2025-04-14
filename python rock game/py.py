import random

round = 0
while round < 5:
    print("Round", round + 1)
    round += 1
    choices = ["rock", "paper", "scissors", "lizard", "spock"]
    user_choice = input("Enter your choice (rock, paper, scissors, lizard, spock): ").lower()
    if user_choice not in choices:
        print("Invalid choice, try again.")
        continue

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and (computer_choice == "scissors" or computer_choice == "lizard")) or \
         (user_choice == "paper" and (computer_choice == "rock" or computer_choice == "spock")) or \
         (user_choice == "scissors" and (computer_choice == "paper" or computer_choice == "lizard")) or \
         (user_choice == "lizard" and (computer_choice == "spock" or computer_choice == "paper")) or \
         (user_choice == "spock" and (computer_choice == "scissors" or computer_choice == "rock")):
        print("You win!")
    else:
        print("You lose!")