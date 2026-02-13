# f = open("demo.txt", "r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()

# Reading a file 
# data = f.read() reads entire file
# data = f.readline() read one line at a time

# f = open("demo.txt", "r")

# line1 = f.readline()
# print(line1)

# line2 = f.readline()
# print(line2)

# overwrite 

# f = open("demo.txt", "r+")
# f.write("Hey")
# print (f.read())
# f.close()


# With syntax

with open("demo.txt", "r") as f:
    data = f.read()
    print(data)

with open("demo.txt", "w") as f:
    f.write("hey this is aayush")


import os

os.remove("sample.txt")