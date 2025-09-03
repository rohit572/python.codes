""" i = columns AND j = rows """
# printing "*" in line :-
for i in range(3):
    for j in range(5,7):
            print("*", end=" ")
    print()


# printing "*" in square pattern :-
for i in range(3):
    for j in range(5,9):
        print("*",end=" ")
    print()


# printing "#" in ractangular shape :-
for i in range(4):
    for j in range(5,12):
        print("#",end=" ")
    print()

# print without line :-
for i in range(1,10):
    print("*",end=" ")
print("\n")

# pattern of 0 using "*" :-
for rows in range(7):
    for columns in range(5):
        if (rows==0 or rows==6) or (columns==0 or columns==4):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# to print a patten of 1 using "*" :-
for row in range (7):
    for col in range(5):
        if (row == 6 or col == 2 or (row == 1 and col < 2)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


# to print a pattern of 2 using :-
for row in range(7):
    for col in range(5):
        if (row == 0 or row == 3 or row == 6 or (col == 4 and row < 3) or (col == 0 and row > 3)):
            print("*" , end = " ")
        else:
            print(" ", end = " ")
    print()

# to print a pattern of 3 using "*" :-
for row in range(7):
    for col in range(5):
        if (row == 0 or row == 3 or row == 6 or col == 4):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# to print a pattern of 4 using "*" :-
for row in range(7):
    for col in range(5):
        if (row == 3 or (col == 4 or (col == 0 and row < 3))):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# to print 5 usinf star :-
for row in range(7):
    for col in range(5):
        if (row == 0 or row == 3 or row == 6 or (col == 0 and row < 3) or (col == 4 and row > 3)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()