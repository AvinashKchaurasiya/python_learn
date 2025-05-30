# with open("file-IO/test.txt", 'w') as f:
#     f.write("Hii everyone\nWe are learning File I/O\nusing Python.\nI like programming in Python")

word = input("Enter word")
with open("file-IO/test.txt", "r") as f:
    data = f.read()
    if(data.find(word) != -1):
        print("found")
    else:
        print("not found")
# with open("file-IO/test.txt", "w") as f:
#     f.write(new_data)