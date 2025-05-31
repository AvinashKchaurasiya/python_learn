list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transpose = []
for i in range(len(list[0])):  # Columns
    row = []
    for j in range(len(list)):  # Rows
        row.append(list[j][i])
    transpose.append(row)
print("Original List:", list)
print("Transposed List:", transpose)
# This code transposes a 2D list (list) and returns a new list