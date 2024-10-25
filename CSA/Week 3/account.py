
class Account:
    username = ''
    password = ''
    id = ''
    fullName = ''
    
    def __init__(self, username, password, fullName, id):
        self.username = username
        self.password = password
        self.id = id
        self.fullName = fullName
    
    def show(self):
        print('Username: ' + self.username)
        print('Password: ' + self.password)
        print('Id: ' + self.id)
        print('Full Name: ' + self.fullName)
    
    # password hợp lệ: có trên 6 kí tự, ít nhất 1 chữ hoa, 1 chữ thường
    # 1 chữ số , 1 kí tự đặc biệt
    def isPasswordValid(self):
        l = len(self.password)
        countA = 0
        counta = 0
        countNumber = 0
        countSpecialCharacter = 0
        for key in self.password:  # duyệt từng kí tự trong password
            if 'A' <= key <= 'Z':
                countA += 1
            elif 'a' <= key <= 'z':
                counta += 1
            elif '0' <= key <= '9':
                countNumber += 1
            else:
                countSpecialCharacter += 1
        if l >= 6 and countA > 0 and counta > 0 and countNumber > 0 and countSpecialCharacter > 0:
            return "Valid"
        return "Invalid"
        
    
ng1 = Account('buiquangvinh9a4', '1234567', '11000', 'Bùi Quang Vinh')
ng1.show()
print(ng1.isPasswordValid())