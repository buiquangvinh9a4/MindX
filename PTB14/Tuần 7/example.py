class MoneyManager:
    def __init__(self):
        # Khởi tạo tài khoản với số dư ban đầu là 0
        self.balance = 0

    def view_balance(self):
        # Hàm xem số dư hiện tại
        print(f"Số dư hiện tại của bạn là: {self.balance} đồng.")

    def deposit(self, amount):
        # Hàm nạp tiền vào tài khoản
        if amount > 0:
            if amount > 1000000:
                bonus = amount * 0.1
                self.balance += amount + bonus
                print(f"Bạn đã nạp {amount} đồng và nhận được thêm {bonus:.0f} đồng (10% tiền thưởng)!")
            else:
                self.balance += amount
                print(f"Bạn đã nạp {amount} đồng vào tài khoản.")
        else:
            print("Số tiền nạp phải lớn hơn 0.")
        self.view_balance()

    def withdraw(self, amount):
        # Hàm rút tiền khỏi tài khoản
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Bạn đã rút {amount} đồng.")
            else:
                print("Số dư không đủ để rút số tiền này.")
        else:
            print("Số tiền rút phải lớn hơn 0.")
        self.view_balance()

def menu():
    manager = MoneyManager()

    while True:
        # Hiển thị menu lựa chọn
        print("\nQuản lý tiền tiêu vặt")
        print("1. Xem số dư")
        print("2. Nạp tiền")
        print("3. Rút tiền")
        print("4. Thoát")
        choice = input("Chọn chức năng (1-4): ")

        if choice == "1":
            manager.view_balance()
        elif choice == "2":
            try:
                amount = int(input("Nhập số tiền muốn nạp: "))
                manager.deposit(amount)
            except ValueError:
                print("Vui lòng nhập số hợp lệ.")
        elif choice == "3":
            try:
                amount = int(input("Nhập số tiền muốn rút: "))
                manager.withdraw(amount)
            except ValueError:
                print("Vui lòng nhập số hợp lệ.")
        elif choice == "4":
            print("Cảm ơn bạn đã sử dụng ứng dụng!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại.")

# Chạy ứng dụng
menu()
