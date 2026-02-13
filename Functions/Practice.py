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


# WAP to find the factorial of n. 
  
def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

cal_fact(5)

# WAP to convert USD to INR

def converter(usd_val):
    inr_val = usd_val * 90
    print(usd_val, "USD =", inr_val, "INR")

converter(100)

# WAP to print EVEN or ODD number.

n = int(input("enter your num : "))

def odd_or_even(n):
    if(n%2==0):
        print("EVEN")
    else:
        print("ODD")

odd_or_even(n)