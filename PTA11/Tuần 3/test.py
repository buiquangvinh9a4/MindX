import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
)

# Lưu trữ thông tin tài khoản (ở đây dùng dictionary để đơn giản)
accounts = {}

class LoginRegisterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Đăng nhập/Đăng ký')

        # Tạo các nút cho giao diện chính
        self.login_button = QPushButton('Đăng nhập')
        self.register_button = QPushButton('Đăng ký')

        # Layout chính
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.login_button)
        main_layout.addWidget(self.register_button)
        self.setLayout(main_layout)

        # Kết nối nút với các chức năng tương ứng
        self.login_button.clicked.connect(self.show_login)
        self.register_button.clicked.connect(self.show_register)

    def show_login(self):
        self.login_window = LoginWindow()
        self.login_window.show()

    def show_register(self):
        self.register_window = RegisterWindow()
        self.register_window.show()

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Đăng nhập')

        # Tạo các widget cho giao diện đăng nhập
        self.username_label = QLabel('Tên đăng nhập:')
        self.password_label = QLabel('Mật khẩu:')
        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.login_button = QPushButton('Đăng nhập')

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        self.setLayout(layout)

        # Kết nối sự kiện
        self.login_button.clicked.connect(self.handle_login)

    def handle_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if username in accounts and accounts[username] == password:
            QMessageBox.information(self, 'Thành công', 'Đăng nhập thành công!')
        else:
            QMessageBox.warning(self, 'Lỗi', 'Tên đăng nhập hoặc mật khẩu không đúng!')

class RegisterWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Đăng ký')

        # Tạo các widget cho giao diện đăng ký
        self.username_label = QLabel('Tên đăng nhập:')
        self.password_label = QLabel('Mật khẩu:')
        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.register_button = QPushButton('Đăng ký')

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.register_button)
        self.setLayout(layout)

        # Kết nối sự kiện
        self.register_button.clicked.connect(self.handle_register)

    def handle_register(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if username in accounts:
            QMessageBox.warning(self, 'Lỗi', 'Tên đăng nhập đã tồn tại!')
        else:
            accounts[username] = password
            QMessageBox.information(self, 'Thành công', 'Đăng ký thành công!')

if __name__ == '__main__':
    app = QApplication(sys.argv)

    main_window = LoginRegisterApp()
    main_window.show()

    sys.exit(app.exec())
