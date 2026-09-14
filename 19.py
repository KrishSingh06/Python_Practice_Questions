# create a class traingle with 3 variables s1,s2,s3 .it also have 3 varaible a1,a2,a3. intialize the variable with constructor
# create a class equilateral traingle and find the area of the traingle with a calarea function.
# find the tangent of all angles using findangle method 

import math

class Triangle:
    def __init__(self, s1, s2, s3, a1, a2, a3):
        self.s1, self.s2, self.s3 = s1, s2, s3
        self.a1, self.a2, self.a3 = a1, a2, a3

class EquilateralTriangle(Triangle):
    def calarea(self):
        return (math.sqrt(3) / 4) * self.s1 ** 2

    def findangle(self):
        print(math.tan(math.radians(self.a1)))
        print(math.tan(math.radians(self.a2)))
        print(math.tan(math.radians(self.a3)))

t = EquilateralTriangle(5, 5, 5, 60, 60, 60)
print("Area =", t.calarea())
t.findangle()



# create h class scalen traingle   which child of traingle. find out the perimeter of traingle with calperimeter function
# find out area  using calarea
# use the math package for computation . print the area as a whole number

import math

class Triangle:
    def __init__(self, s1, s2, s3):
        self.s1, self.s2, self.s3 = s1, s2, s3

class ScaleneTriangle(Triangle):
    def calperimeter(self):
        return self.s1 + self.s2 + self.s3

    def calarea(self):
        s = self.calperimeter() / 2
        return math.sqrt(s * (s-self.s1) * (s-self.s2) * (s-self.s3))

t = ScaleneTriangle(5, 6, 7)

print("Perimeter =", t.calperimeter())
print("Area =", round(t.calarea()))