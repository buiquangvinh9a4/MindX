
class DongVat:
    def __init__(self, ten, tuoi, can_nang):
        self.ten = ten 
        self.tuoi = tuoi 
        self.can_nang = can_nang
    
    def sound(self):
        print("Meo meo")

    def eat(self, food):
        print("Ah,", food, " is very good!")
    

con1 = DongVat("Mèo", 1, 2)
con1.sound()
con1.eat("Sit")
con1.eat("Fish")