from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtCore import QSize
import sys 

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mixue App")
        button = QPushButton("Bấm vào để uống")
        button.setCheckable(True)
        button.clicked.connect(self.bamNut)
        button.clicked.connect(self.kiemTra)

        self.setCentralWidget(button)

        self.setFixedSize(QSize(1000, 700))

    def bamNut(self):
        print("Hello, I'm Clicked")

    def kiemTra(self, check):
        print("Đã bấm?", check)


app = QApplication(sys.argv)

windows = MainWindow()


windows.show()
app.exec()




