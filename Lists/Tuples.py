tup = (1,2,3,4)
print(type(tup))
print(tup)

# Slicing
tup = (1,2,3,4)
print(tup[1:3])

# WAP to ask the user to enter names of their 3 favorite movies and store them in a list.

# movies = []
# movies.append(input("enter 1st movie: "))
# movies.append(input("enter 2nd movie: "))
# movies.append(input("enter 3rd movie: "))

# print(movies)


# WAP to check if a list contains a palindrome of element. (Hint: use copy() method)
list1 = ["m", "a", "a", "m"]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("Not palindrome")

# WAP to count the number of students with the "A" grade in the following tuple.

grade = ("C", "D", "A", "A", "B", "B", "A")
print(grade.count("A"))

# Store the above values in a list and sort them from "A" to "D".

grade = ["C", "D", "A", "A", "B", "B", "A"]
grade.sort()
print(grade)