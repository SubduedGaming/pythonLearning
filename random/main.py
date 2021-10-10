import random
import time

seed = 0
random.seed(seed)
class Player:
    def __init__(self, name):
        self.numberGuessed = 0
        self.name = name
        self.lives = 10
    def __str__(self):
        return self.name
    def placeGuess(self):
        self.playerGuess = input("What do you guess?: ")
    def looseLife(self):
        self.lives = self.lives - 1
        print("ouch")
    def isNumberGuessed(self):
        self.numberGuessed = 1
        print("Congratulations")

class Game:
    def __init__(self):
        self.numberToGuess = 0
    def __str__(self):
        return self.numberToGuess
    def randomNumber(self):
        self.numberToGuess = random.randint(0, 50)
        print("Number Selected")


wantToPlay = input("Do you want to play? yes or no?: ").lower()
while wantToPlay == "yes":
    name = input("What is your name?")
    player = Player(name)
    print(player.name)
    game = Game()
    lives = player.lives
    game.randomNumber()
    numberToGuess = game.numberToGuess
    numberOfTries = 0
    time.sleep(1)
    while lives > 0 and player.numberGuessed == 0:
        numberOfTries = numberOfTries + 1
        player.placeGuess()
        time.sleep(0.5)
        if player.playerGuess == str(numberToGuess):
            print("Well done, you guessed the number correctly!")
            player.isNumberGuessed()
        elif player.playerGuess < str(numberToGuess):
            print("You guessed too low!\nLoose a life ")
            player.looseLife()
        elif player.playerGuess > str(numberToGuess):
            print("You guessed too high!\nLoose a life ")
            player.looseLife()
        print(numberOfTries)

