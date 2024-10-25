class ConNguoi:
    name = 'default'
    age = 0
    id = 0

    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        
    def show(self):
        print(f'Tớ tên là {self.name}, {self.age} tuổi, id: {self.id}')

class HocSinh(ConNguoi):
    mahocsinh = 0

    def __init__(self, name, age, id, mahocsinh):
        ConNguoi.__init__(self, name, age, id)
        self.mahocsinh = mahocsinh
    
    def show(self):
        ConNguoi.show(self)   
        print(f'Mã học sinh: {self.mahocsinh}')  
    
    


nguoi1 = HocSinh('Vinh', 23, 1001, 123456)
nguoi1.show()

    