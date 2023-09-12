import math
class Shape:
    def area(self):
        pass

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

while(True):
    print('1. Area of Triangle    2. Area of Circle     3. Area of Rectangle',"\n")
    choice=int(input('enter your choice'))
    if choice==1:
        b=int(input('enter base\n'))
        h = int(input('enter height\n'))
        triangle = Triangle(b, h)
        print("Area of triangle:", triangle.area())
    elif choice==2:
        r=float(input('enter the radius\n'))
        circle = Circle(r)
        print("Area of circle:", circle.area())
    elif choice==3:
        b=int(input('enter base\n'))
        l = int(input('enter length\n'))
        rectangle = Rectangle(b, l)
        print("Area of rectangle:", rectangle.area())
    else:
        print('invalid choice')
        exit(0)
