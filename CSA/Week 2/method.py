class Tpoint:
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return self.x + other.x, self.y + other.y
    
    def __sub__(self, other):
        return self.x - other.x, self.y - other.y   

    def __str__(self):
        return f'({self.x}, {self.y})'    

p1 = Tpoint(2, 3)
p2 = Tpoint(1, 2)

print(p1 + p2)
print(p1 - p2)

