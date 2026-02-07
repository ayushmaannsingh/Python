#str1= "Ayush"

#Concatenation

str1 = "Ayush"
str2 = "Singh"
print(str1 + " " + str2)

#Length of string

str3 = "Akash"
len1 = len(str3)
print(len1)

str4 = "Singh"
len2 = len(str4)
print(len2)

final_str = str3 + " " + str4
print(final_str)
print(len(final_str))

# Slicing

str5 = "Ayush Singh"
print(str5[1:4])

str6 = "Apple"
print(str6[-3 : -1])

# Write a program user's first name and print its length.
name = input("enter first name : ")
print("length of first name is" , len(name))

# Write a program to find the occurrence of '$' in a String.
countNo = "Hi, $Iam the $ symbol $99.99"
print(countNo.count("$"))