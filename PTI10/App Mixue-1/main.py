from enum import global_str
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
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
        uic.loadUi("ui/adminUi.ui", self)
        self.controller = controller
        self.btn_taikhoan.clicked.connect(self.moTaiKhoan)
        self.btn_mathang.clicked.connect(self.moMatHang)
        self.btn_lichsu.clicked.connect(self.moLichSu)
        self.docTaiKhoan()
        self.docMatHang()
        self.btn_addUser.clicked.connect(self.moThemTaiKhoan)

    def moTaiKhoan(self):
        self.docTaiKhoan()
        self.stackedWidget.setCurrentIndex(0)
    def moMatHang(self):
        self.docMatHang()
        self.stackedWidget.setCurrentIndex(1)
    def moLichSu(self):
        self.stackedWidget.setCurrentIndex(2)
        
    def docTaiKhoan(self):
        with open("db/accounts.json", "r", encoding="utf-8") as f:
            self.data = json.load(f)
            self.bangTaiKhoan.setRowCount(len(self.data))

            for row, item in enumerate(self.data):
                self.bangTaiKhoan.setItem(row, 0, QTableWidgetItem(item["email"]))
                self.bangTaiKhoan.setItem(row, 1, QTableWidgetItem(item["password"]))
                self.bangTaiKhoan.setItem(row, 2, QTableWidgetItem("Fake tên"))

    def docMatHang(self):
        with open("db/items.json", "r", encoding="utf-8") as f:
            self.data = json.load(f)
            self.bangMatHang.setRowCount(len(self.data))

            for row, item in enumerate(self.data):
                self.bangMatHang.setItem(row, 0, QTableWidgetItem(item["id_mathang"]))
                self.bangMatHang.setItem(row, 1, QTableWidgetItem(item["tenMatHang"]))
                self.bangMatHang.setItem(row, 2, QTableWidgetItem(str(item["soLuong"])))
                self.bangMatHang.setItem(row, 3, QTableWidgetItem(str(item["giaTien"])))

    def moThemTaiKhoan(self):
        self.add_user_window = AddUserWindow(self)
        self.add_user_window.show()
        


class AddUserWindow(QMainWindow):
    def __init__(self, parent = None):
        super().__init__()
        uic.loadUi("ui/addUser.ui", self)
        self.btn_add.clicked.connect(self.themTaiKhoan)
    
    def themTaiKhoan(self):
        email = self.edt_email.text()
        password = self.edt_password.text()
        
        with open("db/accounts.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            newAccount = {
                "email": email,
                "password": password
            }
            data.append(newAccount)
            with open("db/accounts.json", "w") as f:
                    json.dump(data, f, indent = 4)
        self.close()





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
