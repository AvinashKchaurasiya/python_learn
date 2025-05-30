def cals_sum(n):
    if(n == 0):
        return 0
    return cals_sum(n-1) + n

n = int(input("Number : "))
sum = cals_sum(n)
print(cals_sum(n))