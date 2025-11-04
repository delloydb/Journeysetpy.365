# learning tuple in python
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)  # Output: (1, 2, 3, 4, 5)

print(my_tuple[0])  # Output: 1
print(my_tuple[2])  # Output: 3
print(my_tuple[-1])  # Output: 5
for item in my_tuple:
    print(item, end=" ")  # Output: 1 2 3 4 5
print()
print(len(my_tuple))  # Output: 5
# Tuples are immutable, so the following operations will raise errors
