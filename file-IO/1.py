# open(file_name, mode) -> open file   mode => read/ write 
# 

# f = open("file-IO/demo.txt", "r")
# print(f.read(5))
# print(type(f.read()))
# f.close()

# f = open("sample.txt", "a")
# f.close()

# with open("sample.txt", "w") as f:
#     data = f.write("Hello bro")
#     print(data)

import os
os.remove("sample.txt")