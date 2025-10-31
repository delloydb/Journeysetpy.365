# learning arithmentic operations in python programming
# This file demonstrates various arithmetic operations in Python.
# Example: Addition, subtraction, multiplication, division, and modulus operations.

# Getting two numbers from the user

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Addition
sum_result = num1 + num2
print("The sum of", num1, "and", num2, "is:", sum_result)

# Subtraction
sub_result = num1 - num2
print("The difference when", num2, "is subtracted from", num1, "is:", sub_result)

# Multiplication
mul_result = num1 * num2
print("The product of", num1, "and", num2, "is:", mul_result)

# Division
if num2 != 0:
    div_result = num1 / num2
    print("The quotient when", num1, "is divided by", num2, "is:", div_result)
else:
    print("Division by zero is not allowed.")

# Modulus
if num2 != 0:
    mod_result = num1 % num2
    print("The remainder when", num1, "is divided by", num2, "is:", mod_result)
else:
    print("Modulus by zero is not allowed.")
