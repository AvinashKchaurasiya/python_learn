class ExtractDIgit:
    def extractDigit(self, num):
        count = 0
        while(num > 0):
            print(num%10)
            num = num//10
            count += 1
        print("cout :", count)

s1 = ExtractDIgit()
num = int(input("Enter Number : "))
s1.extractDigit(num)