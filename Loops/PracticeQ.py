# Print the element of the following list using a loop:
# [1,4,9,16,25,36,49,64,81,100]

nums = [1,4,9,16,25,36,49,64,81,100]

for val in nums:
    print(val)

# Search for a number x in this tuple using loop:

numbers = (1,4,9,16,25,36,49,64,81,100, 49)
x = 49

index = 0
for values in numbers:
    if(values == x):
        print("number found at index", index)
        break
    index +=1