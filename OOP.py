print ("Hello World")

class Monstar:
    def __init__(self,color,age):
        self.age = age
        self.color = color

    def isHorn(self):
        return F"Monster Color {self.color} and he is {self.age} years old"
        

testObject = Monstar("black" , 220)
testObject2 = Monstar("red" , 460)
testObject3 = Monstar("blue" , 920)
print(testObject.isHorn())
print(testObject2.isHorn())
print(testObject3.isHorn())