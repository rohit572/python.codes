year = int(input("Enter the year\n"))

if (year % 400 == 0) or (year % 4 == 0):
    print("year is a leap year")

else:
    print("year is not a leap year")