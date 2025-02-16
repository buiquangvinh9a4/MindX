from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget
from PyQt6 import uic 
import sys




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
            msg = QMessageBox()
            msg.setWindowTitle("Thành công")
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setText("Đăng nhập thành công")
            msg.exec()

            self.window2 = HomePage()
            self.window2.show()
            self.close()

class HomePage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Home Page")

        

app = QApplication(sys.argv)
window = Login()
window.show()
app.exec()