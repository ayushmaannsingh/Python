# WAP to print the lenght of a list. (list in the parameter)

cities = ["delhi", "gurgaon", "noida", "pune", "mumbai", "chennai"]

def printLength(list):
    print (len(list))

printLength(cities)

# WAP to print the elements of a list in a single line.

heroes = ["thor", "ironman", "captain america", "shaktiman"]

def print_len(list):
    print(len(list))

def print_list(list):
    for item in list:
        print(item, end=" ")
    
print_list(heroes)
