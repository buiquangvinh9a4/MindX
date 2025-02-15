import sys
import json
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("TableWidget Example")  # Đặt tiêu đề cửa sổ
        self.resize(400, 300)  # Đặt kích thước cửa sổ mặc định

        # Tạo QTableWidget
        self.tableWidget = QTableWidget(self)
        self.setCentralWidget(self.tableWidget)

        # Đọc dữ liệu từ JSON
        self.load_data_from_json("db/accounts.json")

    def load_data_from_json(self, filename):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                data = json.load(file)

            # Cài đặt số hàng và số cột
            self.tableWidget.setRowCount(len(data))
            self.tableWidget.setColumnCount(2)  # 2 cột: email, password
            self.tableWidget.setHorizontalHeaderLabels(["Email", "Password"])

            # Đổ dữ liệu vào bảng
            for row, item in enumerate(data):
                self.tableWidget.setItem(row, 0, QTableWidgetItem(item["email"]))
                self.tableWidget.setItem(row, 1, QTableWidgetItem(item["password"]))

        except Exception as e:
            print(f"Lỗi khi đọc JSON: {e}")

# Chạy ứng dụng
app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())
