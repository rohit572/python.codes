num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))


# using F-string :-
if num1 % num2 == 0:
    print(f"{num1} is divisible by {num2}")
else:
    print(f"{num1} is divisible by {num2}")

"""OR"""

# without using F-string :-
if num1 % num2 == 0:
    print("\n"+str(num1)+"is divisible by"+str(num2))
else:
    print("\n"+str(num1)+"is not divisible by"+str(num2))  