class Polygon():
    def __init__(self,num):
        # số cạnh = num người dùng nhập vào, độ dài mặc định là 0
        self.num = num # số cạnh
        self.length = [0 for i in range(self.num)]
    
    def input(self):
        # nhập độ dài từng cạnh
        for i in range(self.num):
            self.length[i] = float(input("Length: "))
    
    def output(self):
        for i in range(self.num):
            print(self.length[i])

class TamGiac(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)

    def perermeter(self):
        
        a,b,c = self.length
        if a+b>c or a+c>b or b+c>a:
            return a + b + c
        else:
            print("Invalid")

    def area(self):
        a,b,c = self.length
        nua_chu_vi = (a+b+c)/2
        return (nua_chu_vi*(nua_chu_vi-self.length[0])*(nua_chu_vi-self.length[1])*(nua_chu_vi-self.length[2]))**0.5


class Square(Polygon):
    def __init__(self):
        Polygon.__init__(self,1)
    
    def perermeter(self):
        a = self.length[0]
        return a*4
    
    def area(self):
        a = self.length[0]
        return a*a

class Rectangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,2)
    
    def perermeter(self):
        a,b = self.length
        return a*b
    
    def area(self):
        a,b = self.length
        return a*b


shape = input("Enter shape: ")
if shape == "triangle":
    t = TamGiac()
    t.input()
    print("Chu vi cua tam giac : {}".format(t.perermeter()))
    print("Dien tich tam giac: {}".format(t.area()))

elif shape == "square":
    s = Square()
    s.input()
    print("Chu vi hinh vuong: {}".format(s.perermeter()))
    print("Dien tich hinh vuong: {}".format(s.area()))
elif shape == "rectangle":
    r = Rectangle()
    r.input()
    print("Chu vi hinh chu nhat: {}".format(r.perermeter()))
    print("Dien tich hinh chu nhat: {}".format(r.area()))