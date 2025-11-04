# learning lists in python programming
# example 1: creating and accessing a list
fruits = ["apple", "banana", "cherry", "date"]
print("Fruits list:", fruits)
print("First fruit:", fruits[0])  # Accessing the first item
print("Last fruit:", fruits[-1])  # Accessing the last item

# example 2: modifying a list
fruits[1] = "blueberry"  # Changing 'banana' to 'blueberry'
print("Modified fruits list:", fruits)

# example 3: adding and removing items
fruits.append("elderberry")  # Adding a new fruit
print("After appending:", fruits)
fruits.remove("cherry")  # Removing 'cherry'
print("After removing cherry:", fruits)
# example 4: iterating through a list
print("Fruits in the list:")
for fruit in fruits:
    print(fruit)
# example 5: list methods
print("Number of fruits in the list:", len(fruits))  # Length of the list
