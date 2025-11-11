# this file is used to generate random numbers
import random


def generate_random_number(start, end):
    """Generate a random number between start and end (inclusive)."""
    return random.randint(start, end)


# Example usage
if __name__ == "__main__":
    start = 1
    end = 100
    random_number = generate_random_number(start, end)
    print(f"Random number between {start} and {end}: {random_number}")
