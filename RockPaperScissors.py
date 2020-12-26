#This code tells the user what the game is about, and states the options.

print("This is a game of rock, paper, scissors.  Here's how it works:")
print("You will have to pick rock, paper, or scissors and enter the corresponding number.")
print("YOUR OPTIONS:")
print("1: PAPER \n2: SCISSORS \n3: ROCK \n")
print("Enter your option after the colon:")

#This code evaluates the user's answer, and prints the appropriate message.

answer = int(input())
if answer == 1:
    print("You selected paper.")
if answer == 2:
    print("You selected scissors")
if answer == 3:
        print("You selected rock.")

#This code prompts the computer to pick an answer, and prints the appropriate message.

import random
rock = 3
computer_answer = random.randint(1, rock)
if computer_answer == 1:
    print("Computer picked paper.")
if computer_answer == 2:
    print("Computer picked scissors.")
if computer_answer == 3:
    print("Computer picked rock.")

#This mini-block compares matches where the user and the computer are the same.

if answer == computer_answer:
    print("It's a tie. Try again.")

#This mini-block compares matches where the user is a paper.

if answer == 1 and computer_answer == 2:
    print("You lost. Scissor beats paper.")
if answer == 1 and computer_answer == 3:
    print("You won. Paper beats rock.")

#This mini-block compares matches where the user is a scissor.

if answer == 2 and computer_answer == 1:
    print("You won. Scissor beats paper.")
if answer == 2 and computer_answer == 3:
    print("You lost. Rock beats scissors.")

#This mini-block compares matches where the user is a rock.

if answer == 3 and computer_answer == 1:
    print("You lost. Paper beats rock.")
if answer == 3 and computer_answer == 2:
    print("You won. Rock beats scissors.")

# This block of code prints messages when the user doesn't follow directions.
#
# if answer != range(1,4) or answer != range(:
#     print("DUMMY! LEARN TO READ DIRECTIONS!")
#     print("EVEN A COMPUTER IS SMARTER THAN YOU, SEE!")
