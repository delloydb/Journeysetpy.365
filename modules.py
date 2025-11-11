# learning modules in python programming
# A module is a file containing Python definitions and statements. The file name is the module name with the suffix .py added.
# Modules are used to break down large programs into small manageable and
# organized files. They also provide reusability of code.
# We can define our most used functions in a module and import it, instead of copying their definitions into different programs.
# Example of a module in Python

import converters


print(converters.lbs_to_kg(150))  # Convert 150 pounds to kilograms
# this file is a converter functions file to be used in other modules

numbers = [1, 2, 3, 4, 5]

print(converters.find_max(numbers))  # Output: 5
print(converters.find_min(numbers))  # Output: 1
print(converters.calculate_average(numbers))  # Output: 3.0
print(converters.calculate_sum(numbers))  # Output: 15
