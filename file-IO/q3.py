EvenCount = 0
oddCount = 0
with open("file-IO/test.txt", 'r') as f:
    data = f.read()
    print(data)
    lists = data.split(",")
    print(lists)
    for val in lists:
        if(int(val)%2 == 0):
            EvenCount +=1
        else:
            oddCount += 1
print("Even Number count :",EvenCount)
print("Even Number count :",oddCount)
