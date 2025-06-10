import sys
import json
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

class ProfileApp(QWidget):
    def __init__(self, user_data):
        super().__init__()
        self.user_data = user_data
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Trang Cá Nhân")
        self.resize(900, 500)

        # Layout tổng
        main_layout = QHBoxLayout(self)

        # ==== Bên trái ====
        left_panel = QVBoxLayout()
        name_label = QLabel(f"Xin chào! Tôi là\n<b>{self.user_data['name']}</b>")
        name_label.setStyleSheet("font-size: 24px; color: white;")
        role_label = QLabel(self.user_data['role'])
        role_label.setStyleSheet("font-size: 18px; color: white;")

        left_panel.addWidget(name_label)
        left_panel.addWidget(role_label)
        left_panel.addStretch()

        left_widget = QWidget()
        left_widget.setLayout(left_panel)
        left_widget.setStyleSheet("background-color: #712B75; padding: 40px;")
        left_widget.setFixedWidth(300)

        # ==== Bên phải ====
        right_panel = QVBoxLayout()

        contact_title = QLabel("LIÊN HỆ VỚI TÔI")
        contact_title.setStyleSheet("font-weight: bold; font-size: 20px;")
        right_panel.addWidget(contact_title)

        # Thông tin liên hệ
        info_grid = QGridLayout()
        info_grid.addWidget(QLabel("📍 Địa chỉ:"), 0, 0)
        info_grid.addWidget(QLabel(self.user_data["address"]), 0, 1)
        info_grid.addWidget(QLabel("📞 Điện thoại:"), 1, 0)
        info_grid.addWidget(QLabel(self.user_data["phone"]), 1, 1)
        info_grid.addWidget(QLabel("✉️ Email:"), 2, 0)
        info_grid.addWidget(QLabel(self.user_data["email"]), 2, 1)
        right_panel.addLayout(info_grid)

        # Form liên hệ
        form_layout = QFormLayout()
        form_layout.addRow("Họ và Tên:", QLineEdit())
        sub_layout = QHBoxLayout()
        sub_layout.addWidget(QLineEdit(placeholderText="Số điện thoại"))
        sub_layout.addWidget(QLineEdit(placeholderText="Email"))
        form_layout.addRow(sub_layout)
        form_layout.addRow("Tiêu đề:", QLineEdit())
        form_layout.addRow("Nội dung:", QTextEdit())

        send_btn = QPushButton("Gửi ngay")
        send_btn.setStyleSheet("background-color: #F44336; color: white; padding: 10px;")
        form_layout.addWidget(send_btn)

        right_panel.addLayout(form_layout)

        # Ghép layout
        main_layout.addWidget(left_widget)
        right_widget = QWidget()
        right_widget.setLayout(right_panel)
        main_layout.addWidget(right_widget)

def load_user_data(email):
    with open("db/accounts.json", "r") as f:
        users = json.load(f)
        for u in users:
            if u["email"] == email:
                return u
    return None

if __name__ == "__main__":
    app = QApplication(sys.argv)
    user = load_user_data("admin")  # mặc định
    if user:
        window = ProfileApp(user)
        window.show()
    else:
        print("Không tìm thấy người dùng.")
    sys.exit(app.exec())
