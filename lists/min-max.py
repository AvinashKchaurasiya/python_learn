list = [10, 25, 3, 232, 34, 3, 5]
# def min_max(lst):
#     if not lst:
#         return None, None
#     min_val = lst[0]
#     max_val = lst[0]
#     for num in lst:
#         if num < min_val:
#             min_val = num
#         if num > max_val:
#             max_val = num
#     return min_val, max_val
# min_value, max_value = min_max(list)
# print("Minimum Value:", min_value)
# print("Maximum Value:", max_value)

print("Minimum Value:", min(list))
print("Maximum Value:", max(list))