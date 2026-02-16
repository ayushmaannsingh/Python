# class Student:       # Class
#     name = "Ayush"

# s1 = Student()      # Object
# print(s1.name)

# class Car:
#      color = "blue"
#      brand = "mercedes"
    
# car1 = Car()
# print(car1.color)
# print(car1.brand)

class Student:
    college_name = "Patel college"  # Class attributes

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new student in database")

s1 = Student("Ayush", 94)
print(s1.name, s1.marks)

s2 = Student("Akash", 85)
print(s2.name, s2.marks, s2.college_name)
 
