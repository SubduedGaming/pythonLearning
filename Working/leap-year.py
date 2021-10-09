import time

go = True
while go == True:
    print("This is a leap year calculator. Hope it helps")
    time.sleep(1)
    year = int(input("What year? "))
    y4 = year % 4
    y400 = year % 400
    print(y4)
    print(y400)
    yearType = input("Is the year a century? e.g.2600 or 300 or 1900 [yes or no]").lower()
    if yearType == "yes":
        if y400 == 0:
            print("The year ", year, " is a Leap Year.")
        else:
            print("The year ", year, " is not a Leap Year.")
    else:
        if y4 == 0:
            print("The year ", year, " is a Leap Year.")
        else:
            print("The year ", year, " is not a Leap Year.")









