class Rectangle():
    def __init__(self,height,width):
        self.height = height
        self.width = width
    def input(self):
        self.height = int(input("Height: "))
        self.width = int(input("Width: "))
    def __str__(self):
        return "Rectangle object with height = {} and width = {}".format(self.height,self.width)

rect = Rectangle(1,2)
print(rect)