class Square():
    def __init__(self,side):
        self.side = side
    def cal_area(self):
        return self.side * self.side

square = Square(2)
print('Square area: ',square.cal_area())

class Cube(Square):
    def __init__(self,side):
        Square.__init__(self,side)
    
    def cal_area(self):
        return self.side * self.side * 6
        
    def cal_volume(self):
        return self.side * self.side * self.side

cube = Cube(2)
print('Cube area: ',cube.cal_area())
print('Cube volume: ',cube.cal_volume())