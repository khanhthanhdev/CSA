shape = input("Shape (rectangle|circle): ")

class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def getArea(self):
        print(f"=> Area: {self.height * self.width}")

    def getPerimeter(self):
        print(f"=> Perimeter: {2 * (self.width + self.height)}")


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        print(f"=> Area: {3.14 * self.radius ** 2}")

    def getPerimeter(self):
        print(f"=> Perimeter: {2 * 3.14 * self.radius}")


if shape == "rectangle":
    height = float(input("Height: "))
    width = float(input("Width: "))
    rectangle = Rectangle(height, width)
    rectangle.getPerimeter()
    rectangle.getArea()
elif shape == "circle":
    radius = float(input("Radius: "))
    circle = Circle(radius)
    circle.getPerimeter()
    circle.getArea()
else:
    print("=> Invalid!")