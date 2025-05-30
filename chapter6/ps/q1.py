num1 = int(input("Enter Num1 : "))
num2 = int(input("Enter Num2 : "))
num3 = int(input("Enter Num3 : "))
num4 = int(input("Enter Num4 : "))
if(num1 > num2 and num1 > num3 and num1 > num4):
    print(num1, " Is greatest")
elif(num2 > num1 and num2 > num3 and num2 > num4):
    print(num2, " is greatest")
elif(num3 > num1 and num3 > num2 and num3 > num4):
    print(num3, " is greatest")
else:
    print(num4, " is greatest")