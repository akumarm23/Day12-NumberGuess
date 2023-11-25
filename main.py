# Number Guessing Game v0.1
from art import logo
from random import randint

# Display the game logo
print(logo)

# Constants for difficulty levels
EASY = 10
HARD = 5

def check_answer(guess, answer, turns):
    """Checks the answer against the turns. Returns the number of turns remaining."""
    if guess > answer:
        print("Too High 😅\n")
        return turns - 1
    elif guess < answer:
        print("Too Low 🤨\n")
        return turns - 1
    else:
        print("You WIN!!! 🥳\n")

def set_difficulty():
    # Prompt the user to choose the difficulty level
    level = input("Choose difficulty level: Type 'easy' or 'hard': ").lower()
    # Set the number of turns based on the chosen difficulty level
    if level == 'easy':
        return EASY
    else:
        return HARD

def game():
    print("Welcome to the guessing game!\n")
    print("I am thinking of a number from 1 to 100.\n")
    
    # Generate a random number between 1 and 100 as the answer
    answer = randint(1, 100)
    # For testing purposes, it's a good idea to comment out or remove the next line
    # print("Answer =", answer, "\n")

    # Set the initial number of turns based on the chosen difficulty level
    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} turns left\n")
        # Get the user's guess
        guess = int(input("Make a guess: "))
        # Check the user's guess against the answer and update the number of turns
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("Out of guesses 🥸  You LOST.\n")
            return
        elif guess != answer:
            print("Guess Again. \n")

# Run the game
game()

# END OF CODE
