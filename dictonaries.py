# learning dictornaries in python
# dictionaries are used to store data values in key:value pairs
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates
# Dictionaries are written with curly brackets, and have keys and values

customer = {"name": "John Doe", "age": 30, "is_verified": True}
print(customer)

# accessing values in a dictionary
print(customer["name"])


print(customer["age"])  # using get method with default value

print(customer.get("birthday", 25))  # if key doesn't exist, return default value

# adding a new key-value pair
customer["email"] = " ghrgehrwj@gmail.com"
print(customer)

# updating an existing key-value pair
customer["age"] = 31
print(customer)
