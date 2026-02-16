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
    def __init__(self, fullname):
        self.name = fullname
        print("adding new student in database")

s1 = Student("Ayush")
print(s1.name)

s2 = Student("Akash")
print(s2.name)


