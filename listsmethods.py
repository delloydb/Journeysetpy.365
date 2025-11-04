numbers = [1, 2, 3, 4, 5]
print(numbers.append(6))  # Output: None
print(numbers)  # Output: [1, 2, 3, 4, 5, 6]
print(numbers.pop())  # Output: 6
print(numbers)  # Output: [1, 2, 3, 4, 5]
print(numbers.remove(3))  # Output: None
print(numbers)  # Output: [1, 2, 4, 5]
print(numbers.index(4))  # Output: 2
print(numbers.count(2))  # Output: 1
numbers.sort()
print(numbers)  # Output: [1, 2, 4, 5]
numbers.reverse()
print(numbers)  # Output: [5, 4, 2, 1]

numbers.insert(2, 3)
print(numbers)  # Output: [5, 4, 3, 2, 1]
