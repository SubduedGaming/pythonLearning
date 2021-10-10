import random
import time

class Parent():
    def __init__(self, name, gender):
        self.name = name
        self.hunger = 50
        self.thirst = 50
        self.age = 0
        self.chance1 = 0
        self.chance2 = 0
        self.chanceTotal = 0
        self.dead = False
        self.limit = 100
        self.gender = gender
    def debug(self):
        print("Name: ", str(self.name), "Age: ", str(self.age), "Thirst: ", str(self.thirst), "Hunger: ", str(self.hunger))
    def food(self, choice):
        if self.hunger == 0:
            self.dead = True
        if choice >= 10:
            if self.hunger <= 90:
                print("I eat some food. Yum..That was tasty.")
                randomChance = random.randint(0, 3)
                if randomChance == 1:
                    self.hunger = self.hunger + 10
                elif randomChance == 2:
                    self.hunger = self.hunger + 2
            elif self.hunger > 90:
                print("I'm not hungry right now!")
        elif choice < 7.5:
            print("I cant find any food right now.")
    def aging(self, age):
        if age < self.limit:
            self.age = age + 1
        elif age >= self.limit:
            print("I died of old age")
            self.dead = True
    def water(self, choice):
        if self.thirst == 0:
            self.dead = True
        if choice >= 10:
            if self.thirst <= 90:
                print("I drink some water. Yum..That was refreshing.")
                randomChance = random.randint(0, 3)
                if randomChance == 1:
                    self.thirst = self.thirst + 10
                elif randomChance == 2:
                    self.thirst = self.thirst + 2
            elif self.thirst > 90:
                print("I'm not thirsty right now!")
        elif choice < 7.5:
            print("I cant find any water right now.")
    def choice(self):
        seed = (random.randint(1, 10) * random.randint(10, 20))
        random.seed(seed)
        self.chance1 = random.randint(1, 20)
        self.chance2 = random.randint(1, 20)
        self.chanceTotal = self.chance1 + self.chance2
        self.chanceTotal = self.chanceTotal / 2
        return self.chanceTotal
    def deplete(self, thirst, hunger):
        self.hunger = hunger - 2
        self.thirst = thirst - 2



class Child:
    def __init__(self, hunger, thirst):
        self.hunger = hunger
        self.thirst = thirst
        self.age = 0
        self.chance1 = 0
        self.chance2 = 0
        self.chanceTotal = 0
        self.dead = False
        self.limit = 100
    def debug(self):
        print("Age: ", str(self.age), "Thirst: ", str(self.thirst), "Hunger: ", str(self.hunger))
    def food(self, choice):
        if self.hunger == 0:
            self.dead = True
        if choice >= 10:
            if self.hunger <= 90:
                print("I eat some food. Yum..That was tasty.")
                randomChance = random.randint(0, 3)
                if randomChance == 1:
                    self.hunger = self.hunger + 10
                elif randomChance == 2:
                    self.hunger = self.hunger + 2
            elif self.hunger > 90:
                print("I'm not hungry right now!")
        elif choice < 7.5:
            print("I cant find any food right now.")
    def aging(self, age):
        if age < self.limit:
            self.age = age + 1
        elif age >= self.limit:
            print("I died of old age")
            self.dead = True
    def water(self, choice):
        if self.thirst == 0:
            self.dead = True
        if choice >= 10:
            if self.thirst <= 90:
                print("I drink some water. Yum..That was refreshing.")
                randomChance = random.randint(0, 3)
                if randomChance == 1:
                    self.thirst = self.thirst + 10
                elif randomChance == 2:
                    self.thirst = self.thirst + 2
            elif self.thirst > 90:
                print("I'm not thirsty right now!")
        elif choice < 7.5:
            print("I cant find any water right now.")
    def choice(self):
        seed = (random.randint(1, 10) * random.randint(10, 20))
        random.seed(seed)
        self.chance1 = random.randint(1, 20)
        self.chance2 = random.randint(1, 20)
        self.chanceTotal = self.chance1 + self.chance2
        self.chanceTotal = self.chanceTotal / 2
        return self.chanceTotal
    def deplete(self, thirst, hunger):
        self.hunger = hunger - 2
        self.thirst = thirst - 2