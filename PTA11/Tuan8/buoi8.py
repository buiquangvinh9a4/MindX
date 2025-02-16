from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6 import uic 
import sys

account = {
    "abc1@gmail.com" : "ABC123",
    "abc2@gmail.com" : "ABC123",
}

class DangKy(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("/Users/macos/Documents/HNUE/Programming/MindX/PTA11/Tuan8/dangky.ui", self)
        self.pushButton.clicked.connect(self.checkDangKy)

    def checkDangKy(self):
        email = self.email.text()
        pass1 = self.pass1.text()
        pass2 = self.pass2.text()

        if email in account:
            msg = QMessageBox()
            msg.setWindowTitle("Lỗi")
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setText("Tài khoản đã tồn tại!")
            msg.exec()
        elif pass1 != pass2:
            msg = QMessageBox()
            msg.setWindowTitle("Lỗi")
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setText("Mật khẩu không trùng nhau!")
            msg.exec()
        elif pass1 == pass2:     # đăng ký thành công
            msg = QMessageBox()
            msg.setWindowTitle("Thông báo")
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setText("Đăng ký thành công!")
            msg.exec()

            account[email] = pass1
            print(account)


class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("/Users/macos/Documents/HNUE/Programming/MindX/PTA11/Tuan7/baitap.ui", self)
        self.pushButton.clicked.connect(self.test)

    def test(self):
        usernameAdmin = "admin"
        passwordAdmin = "123456"

        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        
        if len(username) == 0 and len(password) == 0:
            msg = QMessageBox()
            msg.setWindowTitle("Lỗi")
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setText("Bạn chưa nhập gì cả!")
            msg.exec()
        elif usernameAdmin != username or passwordAdmin != password:
            msg = QMessageBox()
            msg.setWindowTitle("Lỗi")
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setText("Tên đăng nhập hoặc tài khoản không chính xác")
            msg.exec()
        else:
            self.home = Home()
            self.home.show()
            self.close()


class Home(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("/Users/macos/Documents/HNUE/Programming/MindX/PTA11/Tuan8/homepage.ui", self)



app = QApplication(sys.argv)
window = DangKy()
window.show()
app.exec()