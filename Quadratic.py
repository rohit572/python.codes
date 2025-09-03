import math

# input coefficients
a = float(input("Enter the coefficient a: \n"))
b = float(input("Enter the coefficient b: \n"))
c = float(input("Enter the coefficient c: \n"))

# Calculate the discriminant
discriminant = b**2 - 4*a*c

# Check if the discriminant is positive, negative, or zero.

if discriminant > 0:
    # Two real and distinct roots
    roots1 = (-b + math.sqrt(discriminant)) / (2*a)
    roots2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"Root 1: {roots1}")
    print(f"Root 2: {roots2}")
elif discriminant == 0:
    # One real root (repeated)
    root = -b / (2*a)
    print(f"Root: {root}")
else:
    # Complex roots
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
    print(f"Root 1: {real_part} + {imaginary_part}i")
    print(f"Root 2: {real_part} - {imaginary_part}i")