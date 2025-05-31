def reverseNumber(num):
    temp = num
    rev = 0
    while(num > 0):
        rem = num%10
        num = num//10
        rev = (rev*10+rem)
    if(rev == temp):
        return True
    else:
        return False

num = int(input("Enter Number : "))
test = reverseNumber(num)
if(test == True):
    print("Yes number is palendram")
else:
    print("not12")