class BankAccount:
    bankname = ''
    username = ''
    password = ''
    
    def __init__(self, bankname, username, password):
        self.__bankname = bankname
        self.__username = username
        self.__password = password
    
    def setUserName(self, user):
        self.__username = user

    def setPassword(self, password):
        self.__password = password       
        
    def show(self):
        print(f'{self.__bankname}')
        print(f'{self.__username} {self.__password}')
        
        
class LocalCard(BankAccount):
    localMoney = 0
    
    def __init__(self, bankname, username, password, localMoney):
        BankAccount.__init__(self, bankname, username, password)
        self.__localMoney = localMoney 
        
    def sendMoney(self, money):
        self.__localMoney += money
        print(f'+ {money} -> {self.__localMoney}')  # hiển thị ra sau khi cộng
        
    def withDraw(self, money):
        if (money > self.__localMoney):
            print('ERROR!')
        else:
            self.__localMoney -= money
            print(f'- {money} -> {self.__localMoney}')  # hiển thị ra sau khi trừ
    
    def checkMoney(self):
        return self.__localMoney 
        
    
    def show(self):
        BankAccount.show(self)
        print(f'{self.__localMoney}')
           

        
account1 = LocalCard('Vietinbank', 'vinhdz', '123456', 50000000)

print(account1.localMoney) 

