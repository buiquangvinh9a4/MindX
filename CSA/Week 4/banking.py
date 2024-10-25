
class BankAccount:
    # Các thuộc tính của class BankAccount
    bankName = ''
    username = ''
    password = ''
    
    # Phương thức khởi tạo cho class BankAccount
    def __init__(self, bankName, username, password):
        self.__bankName = bankName
        self.__username = username
        self.__password = password
        
    # Phương thức khởi tạo giá trị cho bankName của class
    def setUserName(self, username):
        self.__username = username
        
    def getUserName(self):
        return self.__username
    
    # Phương thức khởi tạo giá trị cho username của class
    def setPassword(self, password):
        self.__password = password
        

    # Phương thức hiển thị thông tin các thuộc tính của class
    def show(self):
        print(f'Bank Name: {self.__bankName}')
        print(f'Username: {self.__username}')
        print(f'Password: {self.__password}')
     
      
class LocalCard(BankAccount):          # class LocalCard kế thừa từ class BankAccount
    # khai báo thuộc tính localMoney
    localMoney = 0            
    
    # phương thức __init__() của class LocalCard kế thừa từ phương thức __init__() class BankAccount
    def __init__(self, bankName, username, password, localMoney = 0):
        BankAccount.__init__(self, bankName, username, password)
        self.__localMoney = localMoney
        
    # phương thức rút tiền
    def withdraw(self, money):
        if (money <= self.__localMoney):
            self.__localMoney -= money
            print(f'--> Successfully withdraw: -{money}.')
        else:
            print('--> The balance in the account is not enough!')
    
    # phương thức gửi tiền
    def sendMoney(self, money):
        self.__localMoney += money
        print(f'--> Successfully sent money +{money}')
    
    # phương thức kiểm tra số dư trong tài khoản
    def checkMoney(self):
        return self.__localMoney
    
    # phương thức chuyển khoản từ tài khoản này sang tài khoản LocalCard khác
    def transfer(self, LocalCard, money):
        self.__localMoney -= money
        LocalCard.sendMoney(money)
        print(f'-> Transfer Successfully {money} to {LocalCard.getUserName()}')
    
    # phương thức hiển thị thông tin các thuộc tính của class kế thừa từ phương thức show() class BankAccount
    def show(self):
        BankAccount.show(self)
        print(f'Local Money: {self.__localMoney}')
    

class GlobalCard(BankAccount):          # class GlobalCard kế thừa từ class BankAccount
    # khai báo thuộc tính localMoney
    globalMoney = 0            
    
    # phương thức __init__() của class LocalCard kế thừa từ phương thức __init__() class BankAccount
    def __init__(self, bankName, username, password, globalMoney = 0):
        BankAccount.__init__(self, bankName, username, password)
        self.__globalMoney = globalMoney
        
    # phương thức rút tiền
    def withdraw(self, money):
        if (money <= self.__globalMoney):
            self.__globalMoney -= money
            print(f'--> Successfully withdraw: -{money}.')
        else:
            print('--> The balance in the account is not enough!')

    # phương thức gửi tiền
    def sendMoney(self, money):
        self.__globalMoney += money
        print(f'--> Successfully sent money +{money}')
        
    # phương thức kiểm tra số dư trong tài khoản
    def checkMoney(self):
        return self.__globalMoney
    
    # phương thức chuyển khoản từ tài khoản này sang tài khoản LocalCard khác
    def transfer(self, GlobalCard, money):
        self.__globalMoney -= money
        GlobalCard.sendMoney(money)
        print(f'-> Transfer Successfully {money} to {GlobalCard.getUserName()}')
        
    # phương thức hiển thị thông tin các thuộc tính của class kế thừa từ phương thức show() class BankAccount
    def show(self):
        BankAccount.show(self)
        print(f'Global Money: {self.__globalMoney}')
    
        
        
c1 = LocalCard('Vietinbank', 'buiquangvinh9a4', 'vinh11a44')
c2 = GlobalCard('BIDV', 'dangtrang9x', 'deptrai')
c1.show()

c1.sendMoney(500000)
print(c1.checkMoney())

c1.withdraw(400000)
print(c1.checkMoney())

c1.withdraw(200000)
print(c1.checkMoney())


c2.sendMoney(1000)
c1.transfer(c2, 5000)
print(c1.checkMoney())
print(c2.checkMoney())
