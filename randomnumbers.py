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

# selecting a random element from a list -- a leader for a team


def select_random_leader(members):
    """Select a random leader from the list of members."""
    return random.choice(members)


# Example usage
if __name__ == "__main__":
    team_members = ["Alice", "Bob", "Charlie", "Diana"]
    leader = select_random_leader(team_members)
    print(f"The selected team leader is: {leader}")

members = ["Alice", "Bob", "Charlie", "Diana"]
leader = select_random_leader(members)
print(f"The selected team leader is: {leader}")
