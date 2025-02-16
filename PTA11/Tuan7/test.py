import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window 1")
        self.setGeometry(100, 100, 300, 200)

        # Nút để chuyển sang MainWindow2
        self.button = QPushButton("Go to Window 2", self)
        self.button.clicked.connect(self.open_window2)
        self.button.setGeometry(80, 80, 140, 40)

    def open_window2(self):
        # Đóng cửa sổ hiện tại và mở MainWindow2
        self.window2 = MainWindow2()
        self.window2.show()
        self.close()

class MainWindow2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window 2")
        self.setGeometry(100, 100, 300, 200)

        # Nút để quay lại MainWindow1
        self.button = QPushButton("Go to Window 1", self)
        self.button.clicked.connect(self.open_window1)
        self.button.setGeometry(80, 80, 140, 40)

    def open_window1(self):
        # Đóng cửa sổ hiện tại và mở MainWindow1
        self.window1 = MainWindow1()
        self.window1.show()
        self.close()

# Khởi động ứng dụng
app = QApplication(sys.argv)
main_window = MainWindow1()
main_window.show()
sys.exit(app.exec())
