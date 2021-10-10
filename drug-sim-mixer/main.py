


# risk list
veryLow = 0
low = 1
medium = 2
high = 3
veryHigh = 4
dangerous = 8
deadly = 15

# Drug List [Toxicity, Strength, Mix Strengthening, Addictiveness]
weed = [veryLow, medium, low, veryLow]
Amp = [veryHigh, medium, low, low]
Ecstasy = [high, medium, low, low]
crystalMeth = [veryHigh, high, medium, high]
coke = [veryHigh, veryHigh, medium, high]
heroin = [dangerous, veryHigh, high, veryHigh]
fent = [deadly, dangerous, high, dangerous]

# Ingredients [Toxicity, Strength, Mix Strengthening, Addictiveness]
acetone = [deadly, veryHigh, high, low]
paracetamol = [high, high, low, veryHigh]
nebilanex = [deadly, medium, medium, low]

# Addictives
ibuprofen = [deadly, medium, low, low]
viagra = [high, medium, low, dangerous]

# Fillers
sugar = [low, veryLow, low, veryLow]
bakingSoda = [veryLow, veryLow, veryLow, veryLow]
washingPowder = [dangerous, veryLow, low, veryLow]
salt = [medium, veryLow, low, veryLow]

# Working Ratios out and printing them (magic 3 formula)
print( " risk list \n veryLow = 0 \n low = 1 \n medium = 2 \n high = 3 \n veryHigh = 4 \n dangerous = 8 \n deadly = 15 \n \n Drug List [Toxicity, Strength, Mix Strengthening, Addictiveness] \n weed = [veryLow, medium, low, veryLow] \n Amp = [veryHigh, medium, low, low] \n Ecstasy = [high, medium, low, low] \n crystalMeth = [veryHigh, high, medium, high] \n coke = [veryHigh, veryHigh, medium, high] \n heroin = [dangerous, veryHigh, high, veryHigh] \n fent = [deadly, dangerous, high, dangerous] \n \n Ingredients [Toxicity, Strength, Mix Strengthening, Addictiveness] \n acetone = [deadly, veryHigh, high, low] \n salt = [medium, veryLow, low, veryLow] \n paracetamol = [high, high, low, veryHigh] \n nebilanex = [deadly, medium, medium, low] \n \n Addictives \n ibuprofen = [deadly, medium, low, low] \n viagra = [high, medium, low, dangerous] \n \n Fillers \n sugar = [low, veryLow, low, veryLow] \n bakingSoda = [veryLow, veryLow, veryLow, veryLow] \n washingPowder = [dangerous, veryLow, low, veryLow] \n salt = [medium, veryLow, low, veryLow]\n")
totalWeight = input("What is the total amount of product you would like to make?")
totalWeight = float(totalWeight)
pureDrug = 73.3
addictive = 3.33
filler = 23.33
totalOnePercent = totalWeight / 100
amountRequiredPureDrug = totalOnePercent * pureDrug
amountRequiredAddictive = totalOnePercent * addictive
amountRequiredFiller = totalOnePercent * filler
print("The required amount of pure drug: " + str(amountRequiredPureDrug) + "g\n" + "The required amount of addictive: " + str(amountRequiredAddictive) + "g\n" + "The required amount of filler: " + str(amountRequiredFiller) + "g\n")

# Working out attributes
chosenFiller = input("What will be the filler?").lower()
chosenDrug = input("What will be the chosen drug?").lower()
chosenAddictive = input("What will be the chosen addictive?").lower()

