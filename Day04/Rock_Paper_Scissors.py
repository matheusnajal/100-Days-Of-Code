import Choices
from random import randint

game_images = [Choices.rock, Choices.paper, Choices.scissors]

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print("You chose:")
print(game_images[choice])


computer_choice = randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if choice >= 3 or choice < 0:
    print("You typed an invalid number. You lose!")
elif choice == 0 and computer_choice == 2:
    print("You Win!")
elif computer_choice == 0 and choice == 2:
    print("You Lose!")
elif computer_choice > choice:
    print("You Lose!")
elif choice > computer_choice:
    print("You Win!")
elif choice == computer_choice:
    print("Draw!")