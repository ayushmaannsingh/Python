# Create a new file "practice.txt" using python. Add the folling data in it:

# with open("practice.txt", "w") as f:
#     f.write("Hi everyone\nI am learning File I/O ")
#     f.write("using python.\nI like programming in python.")

# WAF that replace all occurrences of "Python" with "Java" in above file.

# with open("practice.txt", "r") as f:
#     data = f.read()

# new_data = data.replace("python", "java")
# print(new_data)

# with open("practice.txt", "w") as f:
#     f.write(new_data)


# Search if the word "learning" exists in the file or not.

def check_for_word():
    word = "learning"
    with open("practice.txt", "r") as f:
        data = f.read()
        if(data.find(word) !=-1):
            print("Found")
        else:
            print("not found")

check_for_word()