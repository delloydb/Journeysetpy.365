# learning math functions in python programming
# This file demonstrates various mathematical functions in Python.
# Example: Using built-in math functions like sqrt, pow, and abs.
import math

# Getting a number from the user
number = float(input("Enter a number to perform mathematical operations: "))

# Square root
sqrt_result = math.sqrt(number)
print("The square root of", number, "is:", sqrt_result)

# Power
exponent = int(input("Enter an exponent to raise the number to: "))
power_result = math.pow(number, exponent)
print(number, "raised to the power of", exponent, "is:", power_result)

# Absolute value
abs_result = abs(number)
print("The absolute value of", number, "is:", abs_result)

# Rounding the number
rounded_result = round(number)
print("The rounded value of", number, "is:", rounded_result)
