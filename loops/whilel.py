# 1 to 100
# i = 100
# while i >= 1:
#     print(i)
#     i -= 1

# multiple table
# num = int(input("Enter number = "))
# i = 1
# while i <= 10:
#     print(num*i)
#     i += 12

# num = int(input("Enter number = "))
# i = 1
# while i <= num:
#     print(i**2)
#     i += 1

# tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# num = int(input("Enter number = "))
# i = 0
# while i < len(tup):
#     if(num == tup[i]):
#         print("found at ", i)
#         break
#     else:
#         print("Searching...")
#         i += 1 


# sum
num = int(input("Enter number : "))
i = 1
sum = 0
while i <= num:
    sum += i
    i += 1
print("Addition of n natural number =", sum)