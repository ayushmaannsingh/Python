# Super method

class Car_Carr:
    def __init__(self, type):
        self.type = type


    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped.")

class ToyotaCar(Car_Carr):
    def __init__(self, name, type):
        super().__init__(type)
        self.name = name
        super().start()
        

# class Fortuner(ToyotaCar):
#     def __init__(self, type):
#         self.type = type

car1 = ToyotaCar("prius", "electric")
print(car1.type)
# car1.start()


# Class method

class Person:
    name = "anonymous"

    # def changeName(obj, name):
    #     self.__class__.name = "Ayush"

    @classmethod
    def changeName(cls, name):
        cls.name = name


p1 = Person()
p1.changeName("Ayush Singh")
print(p1.name)
print(Person.name)