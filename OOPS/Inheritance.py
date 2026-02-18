# Single Inheritance

class Car:
    color = "black"

    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped.")

class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name

car1 = ToyotaCar("Fortuner")
car2 = ToyotaCar("prius")

print(car1.name)
print(car1.color)

# Multi-level Inheritance

class Car_Car:
    
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped.")

class ToyotaCar(Car_Car):
    def __init__(self, brand):
        self.name = brand

class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type

car1 = Fortuner("disel")
car1.start()

# Multiple Inheritance

class A:
    varA = "welcome to class A"

class B:
    varB = "welcome to class B"

class C: 
    varC = "welcome to class C"

c1 = C()


# print(c1.varC)
# print(c1.varB)
# print(c1.varA)



