# this file is a converter functions file to be used in other modules


def lbs_to_kg(pounds):
    """Convert pounds to kilograms."""
    return pounds * 0.45359237


def kg_to_lbs(kilograms):
    """Convert kilograms to pounds."""
    return kilograms / 0.45359237


def miles_to_km(miles):
    """Convert miles to kilometers."""
    return miles * 1.609344


def km_to_miles(kilometers):
    """Convert kilometers to miles."""
    return kilometers / 1.609344


# Save this code in a file named mymodule.py


def find_max(numbers):
    """Return the maximum number from a list of numbers."""
    if not numbers:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num


def find_min(numbers):
    """Return the minimum number from a list of numbers."""
    if not numbers:
        return None
    min_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
    return min_num


def calculate_average(numbers):
    """Return the average of a list of numbers."""
    if not numbers:
        return None
    return sum(numbers) / len(numbers)


def calculate_sum(numbers):
    """Return the sum of a list of numbers."""
    return sum(numbers)


def calculate_product(numbers):
    """Return the product of a list of numbers."""
    product = 1
    for num in numbers:
        product *= num
    return product


def calculate_variance(numbers):
    """Return the variance of a list of numbers."""
    if not numbers:
        return None
    avg = calculate_average(numbers)
    return sum((x - avg) ** 2 for x in numbers) / len(numbers)


def calculate_stddev(numbers):
    """Return the standard deviation of a list of numbers."""
    variance = calculate_variance(numbers)
    if variance is None:
        return None
    return variance**0.5


def sort_numbers(numbers):
    """Return a sorted list of numbers."""
    return sorted(numbers)


def reverse_numbers(numbers):
    """Return a reversed list of numbers."""
    return list(reversed(numbers))


def unique_numbers(numbers):
    """Return a list of unique numbers."""
    return list(set(numbers))


def count_occurrences(numbers, target):
    """Return the count of occurrences of target in numbers."""
    return numbers.count(target)


def find_median(numbers):
    """Return the median of a list of numbers."""
    if not numbers:
        return None
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    else:
        return sorted_nums[mid]


def find_mode(numbers):
    """Return the mode of a list of numbers."""
    if not numbers:
        return None
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    max_count = max(frequency.values())
    modes = [num for num, count in frequency.items() if count == max_count]
    if len(modes) == 1:
        return modes[0]
    return modes  # Return all modes if there's a tie


# Save this code in a file named mymodule.py
