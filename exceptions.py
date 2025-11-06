# learning how exceptions work in python
# An exception is an event that occurs during the execution of a program that disrupts the normal flow of instructions.
def divide_numbers(num1, num2):
    """Divide two numbers and handle exceptions."""
    try:
        result = num1 / num2
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except TypeError:
        return "Error: Invalid input type. Please provide numbers."
    else:
        return result


# Test the function with different inputs
print(divide_numbers(10, 2))  # Expected output: 5.0
print(divide_numbers(10, 0))  # Expected output: Error: Cannot divide by zero.
print(
    divide_numbers(10, "a")
)  # Expected output: Error: Invalid input type. Please provide numbers.
print(divide_numbers(15, 3))  # Expected output: 5.0
