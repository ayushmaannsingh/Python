# Operator Overloading

print (1 + 2)  #3
print("ayush" + "singh") #Concatenate
print([1,2,3] + [4,5,6])  #merge

# COmplex no.
# Dunder function

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i +", self.img,"j")

num1 = Complex(1, 3)
num1.showNumber()

num2 = Complex(4, 6)
num2.showNumber()