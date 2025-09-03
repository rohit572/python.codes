year = int(input("which year do you wants to checkout?\n"))


if (year % 4 == 0) and (year % 100 == 0):
    print("leap year")

elif (year % 400 == 0) and (year % 100 != 0):
    print("leap year")

else:
    print(" Not leap year")
