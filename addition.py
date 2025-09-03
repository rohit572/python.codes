# Write a Python program to do arithmetical operations addition and division.

# Addition :- 
num1 = float(input("Enter the number for addition\n"))
num2 = float(input("Enter the number for addition\n"))

sum_result = num1 + num2

print(f"sum: {num1} + {num2} = {sum_result}")

# Division :-

num_a = float(input("Enter the first number for division\n"))
num_b = float(input("Enter the second number for division\n"))

if num_b == 0:
    print("Error = Division by zero is not allowed")
else:
    division = num_a/num_b
    
    print(f" Division = {num_a} / {num_b} = {division}")