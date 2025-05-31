list = [1, 2, 3, 4, 5, 6, 2, 3, 2, 3, 11, 12, 13, 14, 15]
unique_list = []
for i in list:
    if i not in unique_list:
        unique_list.append(i)
print("Unique List:", unique_list)
# This code creates a new list containing only the unique elements from the original list.