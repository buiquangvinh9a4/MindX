class Square:
    a = 0
    def __init__(self, a):
        self.a = a
    
    def cal_area(self):
        return self.a * self.a
    
class Cube(Square):  # lớp Cube kế thừa từ lớp Square
    def __init__(self, a):
        Square.__init__(self, a)   # Hàm khởi tạo được kế thừa từ Square
    
    def cal_area(self):
        dientich1mat = Square.cal_area(self)
        return dientich1mat * 6
    
    def cal_volume(self):
        return self.a ** 3
    
square = Square(2)
print('Square area:', square.cal_area())

cube = Cube(2)
print('Cube area:', cube.cal_area())
print('Cube volume:', cube.cal_volume())
