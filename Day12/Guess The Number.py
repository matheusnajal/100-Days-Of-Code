from art import logo
from random import randint
import os

CHANCES_EASY = 10
CHANCES_HARD = 5

def play_game():
    print(logo)
    print("Welcome to the number Guessing Game!\n"
          "I'm thinking of a number between 1 and 100.")
    choose_difficulty = str(input('Chosse a difficulty. Type "easy" or "hard": ').lower())

    if choose_difficulty == "easy":
        print(f"You have {CHANCES_EASY} attempts remaining to guess the number.")
        cont = CHANCES_EASY
    elif choose_difficulty == "hard":
        print(f"You have {CHANCES_HARD} attempts remaining to guess the number.")
        cont = CHANCES_HARD

    computer_number = randint(1, 101)

    while True:
        guess = int(input("Make a guess: "))

        if cont == 1:
            break
        elif guess < computer_number:
            print("Too low.\n"
                  "Guess again.")
            cont -= 1
            print(f"You have {cont} attempts remaining to guess the number.")
        elif guess > computer_number:
            print("Too high.\n"
                  "Guess again.")
            cont -= 1
            print(f"You have {cont} attempts remaining to guess the number.")
        else:
            print(f"You got it! The answer was {computer_number}")
            break

while input("Do you want to play a game of Guess The Number? Type 'y' or 'n': ") == "y":
    os.system('cls')
    play_game()