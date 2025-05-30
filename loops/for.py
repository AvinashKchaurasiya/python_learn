# lists = [1, 2, 3, 4, 5, 6]
# for el in lists:
#     print(el)

# lists = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# for el in lists:
#     print(el)

# tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# num = int(input("Enter number you want to search : "))
# flag = False
# i = 0
# for el in tup:
#     if(el == num):
#         flag = True
#         break
#     else:
#         i += 1
#         print("Searching...")
# if(flag):
#     print(el, "Found at :",i)
# else:
#     print("Not Found at")

# # pass statement
# for i in range(5):
#     pass
# print("hello")


# factoreal

num = int(input("Enter number : "))
fact = 1
for el in range(1, num+1):
    fact *= el
print(fact)