from PyQt6.QtWidgets import QApplication, QVBoxLayout, QMainWindow, QLabel, QWidget
from PyQt6.QtCore import QSize
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vertially Layout")
        self.setFixedSize(QSize(900, 600))

        layout = QVBoxLayout()   # bố cục
        layout.addWidget(QLabel("Ô 1"))   # thêm thành phần cho bố cục
        layout.addWidget(QLabel("Ô 2"))
        layout.addWidget(QLabel("Ô 3"))
        layout.addWidget(QLabel("Ô 4"))


        widget = QWidget()        # màn hình
        widget.setLayout(layout)     # đặt màn hình theo bố cục
        self.setCentralWidget(widget)



app = QApplication(sys.argv)

windows = MainWindow()
windows.show()

app.exec()