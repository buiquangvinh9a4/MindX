class ConNguoi:
    ten = ''
    tuoi = 0
    diachi = ''
    
    def __init__(self, ten, tuoi, diachi):
        self.ten = ten
        self.tuoi = tuoi
        self.diachi = diachi
    
    def show(self):   # hiển thị ra màn hình 3 thuộc tính
        print(self.ten)
        print(self.tuoi)
        print(self.diachi)
    
class HocSinh(ConNguoi):
    mahocsinh = ''
    
    def __init__(self, ten, tuoi, diachi, mahocsinh):
        # kế thừa từ clas ConNguoi
        ConNguoi.__init__(self, ten, tuoi, diachi)
        self.mahocsinh = mahocsinh  # class HocSinh có
    
    def show(self):
        ConNguoi.show(self)
        print(self.mahocsinh)
    

class BacSi(ConNguoi):
    mabacsi = '' 
    def __init__(self, ten, tuoi, diachi, mabacsi):
        ConNguoi.__init__(self, ten, tuoi, diachi)
        self.mabacsi = mabacsi 
    
    def show(self):
        ConNguoi.show(self)
        print(self.mabacsi) 
        

cn1 = ConNguoi("Vinh", 23, "Hà Nội")
hs1 = HocSinh("Linh", 14, "Hà Nội", 705050501)
bs1 = BacSi("Vi", 11, "Hà Nội", 1234567)
hs1.show()
print('---------------')
bs1.show()

