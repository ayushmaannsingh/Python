# WAP to find the sum of first n natural numbers.

n = 5
sum = 0

for i in range(1, n+1):
    sum +=1

print("toatl sum = ",sum)


# WAP to find the factorial of first n natural numbers.

n = 5
fact = 1
# i=1

# while i <= n:
#     fact *=i
#     i +=1

for i in range(1, n+1):
    fact *=i 

print("factorail = ", fact)