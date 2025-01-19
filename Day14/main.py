from art import logo, logo2
from game_data import data
import random
import os

def format_data(account):
    '''Format the account data and returns the printable format.'''
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]

    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(user_guess, a_followers, b_followers):
    '''Take a user's guess and the follower counts and returns if they got it right.'''
    if a_followers > b_followers:
            return user_guess == "a"
    else:
        return user_guess == "b"


print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:

    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}"
        f"{logo2}"
        f"Compare B: {format_data(account_b)}")
        
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"\nYou're right! Current score: {score}\n")
    else:
        print(f"\nSorry, that's wrong. Final Score: {score}\n")
        game_should_continue = False