from math import *
def countDigit(num):
    return int(log10(num)+1)

num = int(input("ENter number : "))
print(countDigit(num))