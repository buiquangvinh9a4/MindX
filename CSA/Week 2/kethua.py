class ConNguoi:
    name = 'default'
    id = 0
    age = 0
    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self.age = age
    def show(self):
        print(f'- Name: {self.name}')
        print(f'- Id: {self.id}')
        print(f'- Age: {self.age}')

class HocSinh(ConNguoi):
    mahocsinh = 0
    def __init__(self, name, id, age, mahocsinh):
        ConNguoi.__init__(self, name, id, age)
        self.mahocsinh = mahocsinh
    def show(self):
        ConNguoi.show(self)
        print(f'- Ma hoc sinh: {self.mahocsinh}')

class BacSi(ConNguoi):
    mabacsi = 0
    def __init__(self, name, id, age, mabacsi):
        ConNguoi.__init__(self, name, id, age)
        self.mabacsi = mabacsi
    def show(self):
        ConNguoi.show(self)
        print(f'- Ma bac si: {self.mabacsi}')


hs1 = HocSinh("Vinh", 10001, 23, 1001000)
hs1.show()