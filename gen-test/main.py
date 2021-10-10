import sys
from genmod import Parent
from genmod import Child


def main():
    sys.stdout = open("out.txt", "w")
    mum = Parent("mum", "female")
    dad = Parent("dad", "male")
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