from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic 
import sys

class Login(QMainWindow):ư
    def __init__(self):
        super().__init__()
        uic.loadUi("/Users/macos/Documents/HNUE/Programming/MindX/PTA11/Tuần 6/mixue.ui", self)

app = QApplication(sys.argv)
window = Login()
window.show()
app.exec()
