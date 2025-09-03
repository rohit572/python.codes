num = int(input("Enter the number: "))

# converted the numbers to a string to easily find the number of digits:
num_str = str(num)
# It stores the length of this string, which is the number of digits in the number:
num_digits = len(num_str)

# To store the sum of the digits raised to power:
sum_of_powers = 0
# a copy of num used for calculation:
temp_num = num

# Calculate the sum of digits raised to the power of num_digits:

while temp_num > 0:
    digit = temp_num % 10
    sum_of_powers += digit ** num_digits
    temp_num //= 10

# Check if it's an armstrong number:
if sum_of_powers == num:
    print(f"{num} is an armstrong number.")
else:
    print(f"{num} is not a armstrong number.")