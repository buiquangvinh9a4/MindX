from enum import global_str
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import Qt
from PyQt6 import uic
import sys
import app_globals
from scripts.controller_file_db import checkAccount  
from scripts.controller_file_db import read_file_db  
from scripts.controller_file_db import write_file_db  
from scripts.controller_file_db import get_role
from admin import AdminUI
db_acc = "App Mixue/db/account.json"


class SignUp(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        uic.loadUi("ui/signUp.ui", self)
        self.setWindowTitle("Sign Up")
        self.controller = controller
        self.error.setText("")
        self.btn_signup.clicked.connect(self.signup_func)
        self.btn_login.clicked.connect(self.goto_login)

    def goto_login(self):
        self.controller.show_login()

    def signup_func(self):
        email = self.edt_email.text()
        password = self.edt_password.text()
        re_password = self.edt_re_password.text()

        result = checkAccount(db_acc, email, password)

        if password != re_password:
            self.error.setText("Password chưa giống nhau. Vui lòng nhập lại!")
        else:
            if result == -1:
                self.error.setText("")
                data = read_file_db(db_acc)
                data.append({'email': email, 'password': password, 'role': 'user'})
                write_file_db(db_acc, data)

                msg = QMessageBox()
                msg.setWindowTitle("Thông báo")
                msg.setIcon(QMessageBox.Icon.Information)
                msg.setText("Đăng ký thành công!")
                msg.exec()
                self.controller.show_login()
                
            else:
                self.error.setText("Email đã tồn tại.")

class Login(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        uic.loadUi("ui/login.ui", self)
        self.setWindowTitle("Login")
        self.error.setText("")
        self.controller = controller
        self.btn_login.clicked.connect(self.btn_login_func)
        self.btn_signup.clicked.connect(self.goto_signup)

    def btn_login_func(self):
        email = self.edt_email.text()
        password = self.edt_password.text()
        result = checkAccount(db_acc, email, password)
        if result == 2:
            app_globals.used_email = email
            role = get_role(db_acc, email)  
            if role == "admin":
                self.controller.show_admin()
            elif role == "user":
                print("Đang phát triển!")
        elif result == 1:
            self.error.setText("Mật khẩu không chính xác.")
        elif result == -1:
            self.error.setText("Tài khoản không tồn tại.")

    def goto_signup(self):
        self.controller.show_signup()



class Controller:
    def __init__(self):
        self.login_window = None
        self.signup_window = None
        self.admin_window = None

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

    def show_admin(self):
        if self.login_window:
            self.login_window.close()
        self.admin_window = AdminUI(self)
        self.admin_window.show()


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
