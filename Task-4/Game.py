import random

print("Welcome to Rock-Paper-Scissors Game!")

while True:
    # User's Input
    user = input("Enter your choice Rock, Paper, or Scissors: ").lower()

    # Computer's Choice
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)

    print("You chose:", user)
    print("Computer chose:", computer)

    # Game Logic
    if user == computer:
        print("It's a Tie!")
    elif user == "rock":
        if computer == "scissors":
            print("You Win! Rock beats Scissors.")
        else:
            print("You Lose! Paper beats Rock.")
    elif user == "paper":
        if computer == "rock":
            print("You Win! Paper beats Rock.")
        else:
            print("You Lose! Scissors beat Paper.")
    elif user == "scissors":
        if computer == "paper":
            print("You Win! Scissors beat Paper.")
        else:
            print("You Lose! Rock beats Scissors.")
    else:
        print("Invalid choice! Please type Rock, Paper, or Scissors.")

    # Play Again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! Goodbye 👋")
        break
        
