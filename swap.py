# input the two varibles
a = input("Enter the value of the first variable\n")
b = input("Enter the values of the second variable\n")

# print the original values
print(f"Original values: a = {a} , b = {b}")

# Swap the values using a temperary variables
temp = a 
a = b
b = temp 

# print the swapped values
print(f"swapped values: a = {a}, b = {b}")