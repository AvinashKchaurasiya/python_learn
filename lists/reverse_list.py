list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
def reverse_list(list):
    reverse_list = []
    for i in range(len(list) - 1, -1, -1):
        reverse_list.append(list[i])
    return reverse_list
print("Original List:", list)
print("Reversed List:", reverse_list(list))
# This code reverses the original list and returns a new list containing the elements in reverse order.