# learning return statements in functions and paramenters in python all together
# A return statement is used to exit a function and return a value to the caller.


def square(number):
    """Return the square of a number."""
    return number * number


result = square(5)
print(f"The square of 5 is {result}")
result = square(10)
print(f"The square of 10 is {result}")
