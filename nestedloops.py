# learning nested for loop looping in practice using python programming

for x in range(4):
    for y in range(3):
        print(f"{x}, {y}")

# example 2: printing a pattern using nested loops
rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end="")
    print("")  # for new line after each row
