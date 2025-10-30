# learning type conversion in python programming
# This file demonstrates how to convert input data types using type conversion functions.
# Example: Converting user's age and height from string to integer and float respectively.

# Getting user's date of birth
date_of_birth = input("Enter your date of birth (YYYY-MM-DD): ")
print("Your date of birth is " + date_of_birth + ".")

# using current year to calculate the age
current_year = 2024
birth_year = int(
    date_of_birth.split("-")[0]
)  # Extracting year and converting to integer
age = current_year - birth_year
print("You are " + str(age) + " years old.")

# Getting user's height and converting to float
user_height = input("Enter your height in feet: ")
height_in_feet = float(user_height)  # Converting string input to float
print("Your height is " + str(height_in_feet) + " feet.")
