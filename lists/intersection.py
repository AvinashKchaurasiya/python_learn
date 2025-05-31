list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
def intersection(list1, list2):
    intersection_list = []
    for i in list1:
        if i in list2 and i not in intersection_list:
            intersection_list.append(i)
    return intersection_list
print("Intersection of two lists:", intersection(list1, list2))