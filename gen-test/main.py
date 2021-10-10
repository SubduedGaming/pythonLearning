import time
import random
import sys

class Parent():
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.thirst = 50
        self.age = 0
        self.chance1 = 0
        self.chance2 = 0
        self.chanceTotal = 0
        self.dead = False
        self.limit = 100
    def debug(self):
        print("Name: ", str(self.name), "Age: ", str(self.age), "Thrist: ", str(self.thirst), "Hunger: ", str(self.hunger))
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
        print("Age: ", str(self.age), "Thrist: ", str(self.thirst), "Hunger: ", str(self.hunger))
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





def main():
    sys.stdout = open("out.txt", "w")
    mum = Parent("mum")
    dad = Parent("dad")
    go = True
    mTold = False
    dTold = False
    while go == True:
        #time.sleep(4)
        print("\n")
        if mum.dead == False:
            mum.deplete(mum.thirst, mum.hunger)
            print(mum.debug())
            if mum.thirst < 90:
                mum.choice()
                mum.water(mum.chanceTotal)
            if mum.hunger < 90:
                mum.choice()
                mum.food(mum.chanceTotal)
            mum.aging(mum.age)
        elif mum.dead == True and mTold == False:
            print("I'm sorry, but mum died. she died at age: ", mum.age)
            print(mum.debug())
            mTold = True
        #time.sleep(4)
        print("\n")
        if dad.dead == False:
            dad.deplete(dad.thirst, dad.hunger)
            print(dad.debug())
            if dad.thirst < 90:
                dad.choice()
                dad.water(dad.chanceTotal)
            if dad.hunger < 90:
                dad.choice()
                dad.food(dad.chanceTotal)
            dad.aging(dad.age)
        elif dad.dead == True and dTold == False:
            print("I'm sorry, but dad died. He died at age: ", dad.age)
            dTold = True
            print(dad.debug())
        if mTold and dTold == True:
            print("Parents are dead")
            break
    sys.stdout.close()



main()
'''
mum = Parent()
for i in range(5):
    time.sleep(1)
    print(mum.thirst)
    print(mum.hunger)
    if mum.thirst < 90:
        mum.water(mum.chanceTotal)
    mum.deplete(mum.thirst, mum.hunger)
'''