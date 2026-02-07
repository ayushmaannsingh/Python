# light = "pink"

# if(light == "green"):
#     print("go")
# elif(light == "red"):
#     print("stop")
# elif(light == "yellow"):
#     print("wait")
# else:
#     print("light is broken")

# print("end of code")

# Grade students based on marks

marks = int(input("enter student marks : "))

if (marks >= 90):
    grade = "A"
elif(marks >= 80 and marks < 90):
    grade = "B"
elif(marks >= 70 and marks < 80):
    grade = "C"
else:
    grade = "D"

print("grade of the student ->", grade)
