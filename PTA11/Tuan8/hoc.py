from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget
from PyQt6 import uic 
import sys

accounts = {}


class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("//Users//macos//Documents//HNUE//Programming//MindX//PTA11//Tuan8//baitap.ui", self)
        self.pushButton.clicked.connect(self.test)

    def test(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        
        if len(username) == 0 and len(password) == 0:
            msg = QMessageBox()
            msg.setWindowTitle("Lỗi")
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setText("Bạn chưa nhập gì cả!")
            msg.exec()
        accounts[username] = password
        print(accounts)
        


class HomePage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Home Page")

        

app = QApplication(sys.argv)
window = Login()
window.show()
app.exec()