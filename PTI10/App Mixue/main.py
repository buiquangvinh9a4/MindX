from enum import global_str
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import Qt
from PyQt6 import uic
import sys
import json


class Login(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        uic.loadUi("ui/login.ui", self)
        self.controller = controller
        # đăng ký: ok
        self.btn_signup.clicked.connect(self.open_signUp)

        # đăng nhập: đang xử lý
        self.btn_login.clicked.connect(self.open_homepage)
    
    def open_signUp(self):
        self.controller.show_signup()

    def open_homepage(self):
        email = self.edt_email.text()
        password = self.edt_password.text()

        isEmailValid = False
        password_user = ""

        with open("db/accounts.json", "r") as f:
            # 1.  tìm email trong json xem có không
            data = json.load(f)
            for user in data:
                if user["email"] == email:
                    isEmailValid = True
                    password_user = user["password"]
                    break    

            # 2. nếu tìm thấy, so sánh password
            if isEmailValid == True:
                if password == password_user:
                    self.controller.show_homepage()

                else:
                    print("Mật khẩu không hợp lệ!")
            else:
                print("Tài khoản không tồn tại!")



class SignUp(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        uic.loadUi("ui/signUp.ui", self)
        self.controller = controller
        self.btn_login.clicked.connect(self.open_login)
        self.btn_signup.clicked.connect(self.click_signUp)

    def open_login(self):
        self.controller.show_login()

    def click_signUp(self):
        email = self.edt_email.text()
        password = self.edt_password.text()
        re_password = self.edt_re_password.text()

        isEmailValid = False
        with open("db/accounts.json", "r") as f:
            # 1.  tìm email trong json xem có không
            data = json.load(f)
            for user in data:
                if user["email"] == email:
                    isEmailValid = True
                    break 
        
        # nếu chưa tồn tại email trong json 
        if isEmailValid == False:
        
            if password == re_password:
                data = []
                with open("db/accounts.json", "r") as f:
                    data = json.load(f)
                    new_account = {
                        "email": email,
                        "password": password
                    }
                    data.append(new_account)

                with open("db/accounts.json", "w") as f:
                    json.dump(data, f, indent = 4)
        else:
            print("Tài khoản đã tồn tại!")
            
            

class HomePage(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        uic.loadUi("ui/admin_ui.ui", self)
        self.controller = controller
        self.btn_show_accounts.clicked.connect(self.open_accounts)
        self.btn_show_items.clicked.connect(self.open_items)
        self.stackedWidget.setCurrentIndex(0)

    def open_accounts(self):
        self.stackedWidget.setCurrentIndex(0)
    
    def open_items(self):
        self.stackedWidget.setCurrentIndex(1)

class Controller:
    def __init__(self):
        self.login_window = None
        self.signup_window = None
        self.homepage_window = None

    def show_login(self):
        if self.signup_window:
            self.signup_window.close()
        self.login_window = Login(self)
        self.login_window.show()

    def show_signup(self):
        if self.login_window:
            self.login_window.close()
        self.signup_window = SignUp(self)
        self.signup_window.show()

    def show_homepage(self):
        if self.login_window:
            self.login_window.close()
        self.homepage_window = HomePage(self)
        self.homepage_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Đặt style "Fusion" để kiểm soát giao diện
    app.setStyle('Fusion')

    # Tạo palette sáng
    palette = QPalette()
    palette.setColor(QPalette.ColorRole.Window, QColor(255, 255, 255))  # Màu nền trắng
    palette.setColor(QPalette.ColorRole.WindowText, QColor(0, 0, 0))  # Màu chữ đen
    palette.setColor(QPalette.ColorRole.Base, QColor(240, 240, 240))  # Màu nền cho ô nhập liệu
    palette.setColor(QPalette.ColorRole.Text, QColor(0, 0, 0))  # Màu chữ trong ô nhập liệu
    palette.setColor(QPalette.ColorRole.Button, QColor(255, 255, 255))  # Nền nút
    palette.setColor(QPalette.ColorRole.ButtonText, QColor(0, 0, 0))  # Màu chữ nút
    app.setPalette(palette)

    # Tạo controller để quản lý màn hình
    controller = Controller()
    controller.show_login()

    sys.exit(app.exec())
