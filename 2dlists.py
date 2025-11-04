# learning 2D lists in python using matrix

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(matrix)
print(matrix[0])  # prints the first row
print(matrix[1][2])  # prints the element at second row and third column
print(matrix[2][1])  # prints the element at third row and second column
for row in matrix:
    for item in row:
        print(item, end=" ")
    print()
# prints all elements in the matrix row by row
