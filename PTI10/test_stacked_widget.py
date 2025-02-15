import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QStackedWidget, QLabel

class AdminDashboard(QWidget):
    def __init__(self):
        super().__init__()

        # Khởi tạo giao diện
        self.setWindowTitle("Admin Dashboard")
        self.setGeometry(100, 100, 600, 400)

        # Tạo các widget cần thiết
        self.stacked_widget = QStackedWidget(self)

        # Tạo các màn hình
        self.home_screen = QLabel("Home Screen")
        self.settings_screen = QLabel("Settings Screen")
        self.users_screen = QLabel("Users Screen")

        # Thêm các màn hình vào QStackedWidget
        self.stacked_widget.addWidget(self.home_screen)
        self.stacked_widget.addWidget(self.settings_screen)
        self.stacked_widget.addWidget(self.users_screen)

        # Tạo các button điều hướng
        self.home_button = QPushButton("Home")
        self.settings_button = QPushButton("Settings")
        self.users_button = QPushButton("Users")

        # Kết nối các button với hàm điều hướng
        self.home_button.clicked.connect(self.show_home)
        self.settings_button.clicked.connect(self.show_settings)
        self.users_button.clicked.connect(self.show_users)

        # Layout cho button
        button_layout = QVBoxLayout()
        button_layout.addWidget(self.home_button)
        button_layout.addWidget(self.settings_button)
        button_layout.addWidget(self.users_button)

        # Layout cho toàn bộ giao diện
        layout = QVBoxLayout()
        layout.addWidget(self.stacked_widget)
        layout.addLayout(button_layout)

        self.setLayout(layout)

    def show_home(self):
        self.stacked_widget.setCurrentIndex(0)

    def show_settings(self):
        self.stacked_widget.setCurrentIndex(1)

    def show_users(self):
        self.stacked_widget.setCurrentIndex(2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AdminDashboard()
    window.show()
    sys.exit(app.exec())
