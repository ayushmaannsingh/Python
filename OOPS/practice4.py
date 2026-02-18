# Define a Employee class with attribute role, department and salary. This class showDetails() method.
# Create an Engineer class that inherits properties from employee , salary and attributes : name and age.

class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("role=", self.role)
        print("dept=", self.dept)
        print("salary=", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "75,000")


engg1 = Engineer("Ayush Singh", 22)
engg1.showDetails()