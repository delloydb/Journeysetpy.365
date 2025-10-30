# learning strings in python programming
# This file demonstrates various string operations in Python.
# Example: Concatenation, repetition, indexing, and slicing of strings.

# Getting user's first and last name
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = first_name + " " + last_name  # Concatenation of strings
print("Hello, " + full_name + "!")

# simple string printing
print("Welcome to the world of Python strings.")

# large string with triple quotes
large_string = """Python is a powerful programming language.
It is widely used for web development, data analysis, artificial intelligence, and more."""
print(large_string)

# large paragraph with single triple quotes
email_body = """Dear User,
Thank you for joining our platform. 

We are excited to have you on board.

Best regards,
"""
print(email_body)

# String repetition
repeat_string = "Python! " * 3
print(repeat_string)

# String indexing and slicing
sample_string = "Programming"
first_character = sample_string[0]  # Indexing
print("First character of '" + sample_string + "' is: " + first_character)
substring = sample_string[0:6]  # Slicing
print("Substring of '" + sample_string + "' from index 0 to 5 is: " + substring)

# Accessing last character using negative indexing
last_character = sample_string[-1]
print("Last character of '" + sample_string + "' is: " + last_character)

# formmating strings
course = "python programming"
print = course.replace("python", "Python").title()  # Replacing and title casing
