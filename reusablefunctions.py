# learning how to create reusable functions in python
# A reusable function is a block of code that can be called multiple times throughout a program,
# allowing for code reuse and modularity.


def calculate_area(length, width):
    """Return the area of a rectangle."""
    return length * width


area1 = calculate_area(5, 10)
print(f"The area of the rectangle with length 5 and width 10 is {area1}")
