lists = ["a", "b", "c", "d"]
def print_list(lists, i):
    if(i == len(lists)):
        return
    print(lists[i])
    print_list(lists, i+1)

print_list(lists, 0)