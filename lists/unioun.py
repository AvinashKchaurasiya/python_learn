list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
def union(list1, list2):
    unnion_list = []
    for i in list1:
        if i not in unnion_list:
            unnion_list.append(i)
    for i in list2:
        if i not in unnion_list:
            unnion_list.append(i)
    return unnion_list
print("Union of two lists:", union(list1, list2))