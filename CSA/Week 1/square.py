from turtle import width


class Rectangle:
    width = 0
    height = 0
    def __init__(self, w, h):
        self.width = w
        self.height = h
    
    def getPerimeter(self):
        return (self.width + self.height) * 2

    def getArea(self):
        return self.width * self.height
    
class Circle:
    radius = 0
    def __init__(self, r):
        self.radius = r
    
    def getPerimeter(self):
        return 3.14 * self.radius * 2
    
    def getArea(self):
        return 3.14 * self.radius * self.radius


shape = input('Rectangle|Circle: ')
if shape == "Rectangle":
    height = float(input('Height: '))
    width = float(input('Width: '))
    rectangle = Rectangle(width, height)
    print(f'=> Perimeter: {rectangle.getPerimeter()}')
    print(f'=> Area: {rectangle.getArea()}')
elif shape == "Circle":
    radius = float(input('Radius: '))
    circle = Circle(radius)
    print(f'=> Perimeter: {circle.getPerimeter()}')
    print(f'=> Area: {circle.getArea()}')        
else:
    print('Invalid!')
        
