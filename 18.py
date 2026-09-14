# create a class shape with varaible radius intialize variable with constructor
# create a class of circle , which child of shape class . Define a method calarea to calculate the area of circle using math package.
# create a class sphere which is child of shape class .Define calvolume to calculate the value of the sphere

import math

# Parent class
class Shape:
    def __init__(self, radius):
        self.radius = radius


# Child class: Circle
class Circle(Shape):
    def calarea(self):
        area = math.pi * self.radius ** 2
        return area


# Child class: Sphere
class Sphere(Shape):
    def calvolume(self):
        volume = (4 / 3) * math.pi * self.radius ** 3
        return volume


# Create objects
r = int(input("Enter radius: "))

circle = Circle(r)
sphere = Sphere(r)

print("Area of Circle =", circle.calarea())
print("Volume of Sphere =", sphere.calvolume())