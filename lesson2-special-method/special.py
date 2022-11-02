

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self,other):
        temp = Point(0,0) # point để giữ kết quả
        temp.x = self.x + other.x
        temp.y = self.y + other.y
        return temp
    def __sub__(self,other):
        temp = Point(0,0)
        temp.x = self.x - other.x
        temp.y = self.y - other.y
        return temp
    
    def __str__(self):
        return "tọa độ x {},tọa độ y {}".format(self.x,self.y)

x = Point(1,2) #gọi hàm __init__
y = Point(3,4) #gọi hàm __init__
z = x+y #gọi hàm __add__
print(z)

g = x-y #gọi hàm __sub__
print(g)
    