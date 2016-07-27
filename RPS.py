
#! Python 3
# Rock Paper Scissor game

import random
import sys


print("Welcome to Rock Paper Scissor")
print("You have to choose between: rock, paper, scissor. Then you might win.")
print("You play 3 rounds!")

# winning conditions as tubles together - order in tuples is important later
winning = [("paper", "rock"),
           ("scissor", "paper"),
           ("rock", "scissor")]


# function if the player wants to play again
def again():
    while True:
        print("=" * 24)
        print("Play again? y/n ?")
        answer = input("> ")
        if answer == "y":
            game()
        elif answer == "n":
            sys.exit(0)
        else:
            print("Enter something valid!")
            continue


# the players plays 3 rounds of RPS, this scripts counts
def game():
    rps = ["rock", "paper", "scissor"]
    rounding = 0  # i choose "rounding" - accidently typing round() was eliminated
    count_pc = 0
    count_player = 0

    while rounding < 3:
        print("What is your guess?")
        choice = input("> ")
        choice = choice.replace(" ", "")  # removes accidently pressed spaces
        print("=" * 18)  # just for the look
        if choice not in rps:
            print("Enter something valid")
            continue

        elif choice == random.choice(rps):
            print("It's a tie! Again!")
            continue
        elif (choice, random.choice(rps)) in winning:
            print("you won!")
            count_player += 1
            print("Computer:", count_pc, "//", "Player:", count_player)
            rounding += 1
            continue
        else:
            print("The PC won!")
            count_pc += 1
            print("Computer:", count_pc, "//", "Player:", count_player)
            rounding += 1
            continue


game()
again()
