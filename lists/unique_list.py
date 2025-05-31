list = [1,2,2,3,4,3,4,2,56,6,5,6,56,56,5,5,5,6,6,6]
unique_list = []
for i in list:
    if i not in unique_list:
        unique_list.append(i)
print("Unique List : ", unique_list)