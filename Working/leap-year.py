year = int(input("What year? "))
year_4 = year % 4
year_100 = year % 100
year_400 = year % 400

if type(year_4) is int and type(year_100) is int and type(year_400) is int:
    print("The year", year, "is a leap year")
    if type(year_100) is float and type(year_400) is float:
        print("Year not leap")
if type(year_4) is int:
    print("leap year")



