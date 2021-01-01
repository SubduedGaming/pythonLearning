#Start
from random import randint
import time



ai = randint(1,3)
#1 = rock
#2 = paper
#3 = scissors

#setting ai choice
ai_choice = ""
if ai == 1:
    ai_choice = "r"
elif ai == 2:
    ai_choice = "p"
elif ai == 3:
    ai_choice = "s"
play_again = 1

while play_again == 1:
    play_again = 0
    player1 = input("What is your choise? R,P,S ").lower()
    print(ai_choice)
    time.sleep(1)
    if ai == 1 and player1 == "p":
        print("player 1 wins")
    elif ai == 2 and player1 == "s":
        print("player 1 wins")
    elif ai == 3 and player1 == "r":
        print("player 1 wins")
    elif ai_choice == player1:
        print("you draw")
    else:
        print("You loose")
    print("Would you like to play again? 1=yes 0=no")
    play_again = int(input())