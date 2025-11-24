import random

WIN_MESSAGE = "Congratulations, you won!"
LOSE_MESSAGE = "Oh, the computer won. It's ok."
TIE_MESSAGE = "Oh, it's a tie."

def random_choice(options=["rock", "paper", "scissors"]):
    return random.choice(options)

def determine_winner(choice1, choice2):
    """
    Determines the winning choice between two choices from selectable options: "rock", "paper", or "scissors".
    Returns the winning choice (e.g. "paper"), or None if there is a tie.
    Example: determine_winner("rock", "paper")
    """

    winners = {
        "rock":{
            "rock": None, 
            "paper": "paper",
            "scissors": "rock",
        },
        "paper":{
            "rock": "paper",
            "paper": None, 
            "scissors": "scissors",
        },
        "scissors":{
            "rock": "rock",
            "paper": "scissors",
            "scissors": None, 
        },
    }

    winner = winners[choice1][choice2]

    return winner

if __name__ == "__main__":

    print("-------------------")
    print("Launching the game...")
    print("-------------------")

    options = ["rock", "paper", "scissors"]

    while True:
        user_choice = input("Please choose either 'rock', 'paper', or 'scissors': ").strip().lower()
        if user_choice in options:
            print("You chose:", user_choice)
            break
        else:
            print("Expecting one of: 'rock', 'paper', or 'scissors' (lower case, without the quotation marks). Please try again.")

    computer_choice = random_choice(options)
    print("The computer chose:", computer_choice)
    print("-------------------")

    winning_choice = determine_winner(user_choice, computer_choice)

    if winning_choice:
        if winning_choice == user_choice:
            print(WIN_MESSAGE)
        elif winning_choice == computer_choice:
            print(LOSE_MESSAGE)
    else:
        print(TIE_MESSAGE)

    print("Thanks for playing. Please play again!")
