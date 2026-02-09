# dict = {
#     "name" : "Ayush",
#     "cgpa" : 8.5,
#     "marks" : [90,80,85],
# }
# print(dict)

# info = {
#     "name" : "AYush Singh",
#     "Subjects" : ["python", "C," "Java",],
#     "topics" : ("dict", "set"),
#     "age" : 35,
#     "is_adult" : True,
#     "marks" : 94.4
# }

# info["age"] = 20
# print(info)

# null_dict = {}
# null_dict["middlename"] = "Kumar"
# print(null_dict)

# Nested Dictionary

student = {
    "name" : "Ayush Singh",
    "subjects" : {
        "Maths" : 94,
        "Chem" : 97,
        "Phy" : 95
    }
}

print(student["subjects"]["Maths"])