import random

# Define the choices
choices = ["rock", "paper", "scissors"]

# Get the user's choice
print("Welcome to Rock, Paper, Scissors game!")
user_choice = input("Choose rock, paper, or scissors: ").lower()

# Check if the user's choice is valid
if user_choice not in choices:
    print("Invalid choice. Please choose rock, paper, or scissors next time.")
else:
    # Step 4: Generate the computer's choice
    computer_choice = random.choice(choices)
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("You win!")
    else:
        print("Computer wins!")
