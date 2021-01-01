from random import seed
from random import randint

#Variables
global old_enough
old_enough = "false"
global points
points = 0
global lives
lives = 3
global name
name = ""

def chance():
    seed()
    chance_win = randint(1, 10)



def age_verify():
    global old_enough
    global name
    name = input("Welcome, What is your name? ")
    print("Hello ", name + ".", "How old are you?")
    age = input()
    if age >= "18":
        old_enough = "true"
    else:
        print("Sorry you are too young for this game")

def game():
    global points
    global lives
    number = randint(0, 20)
    next_number = randint(0, 20)
    print("1st Number = ", number)
    high_low = input("Higher or Lower? ").lower()
    if high_low == "higher":
        print("2nd Number = ", next_number)
        if next_number >= number:
            points += 1
            print("points = ", points)
        else:
            lives -= 1
            print("lives = ", lives)
    elif high_low == "lower":
        print("2nd Number = ", next_number)
        if next_number <= number:
            points += 1
            print("points = ", points)
        else:
            lives -= 1
            print("lives = ", lives)

def leaderboard():
    global text_file
    text_file = open("leaderboard.txt", "a")
    text_file.write(name + ",")
    text_file.write(" " + str(points))
    text_file.write("\n")


age_verify()

#debug age
#old_enough = "true"

while old_enough == "true" and lives > 0:
    game()
else:
    lives = 3
    leaderboard()


