class Tpoint:
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # Tpoint + other    A + B
    def add(self, other):
        return self.x + other.x, self.y + other.y
    
    def __add__(self, other):
        return self.x + other.x, self.y + other.y
    
    def __sub__(self, other):
        return self.x - other.x, self.y - other.y
    
    def __str__(self):
        return f'{self.x}, {self.y}'
    
    def sosanh(self, other):
        if (self.x == other.x):
            return True
        else:
            return False
    def __eq__(self, other):
        if (self.x == other.x):
            return True
        else:
            return False
    
A = Tpoint(2, 3)
B = Tpoint(1, 2)

# Tpoint = B  , other = A
# self.x - other.x, self.y - other.y
#   B.x - A.x , B.y - A.y
#   B - A  ->  kết quả

print(A - B)
print(A.sosanh(B))
print(A == B)