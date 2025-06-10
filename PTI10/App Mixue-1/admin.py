# from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidget, QTableWidgetItem
# from PyQt6.QtGui import QPalette, QColor
# from PyQt6.QtCore import Qt
# from PyQt6 import uic
# import sys
# import json
# from scripts.controller_file_db import checkAccount  
# from scripts.controller_file_db import read_file_db  
# from scripts.controller_file_db import write_file_db  

# db_acc = "db/account.json"

# class AdminUI(QMainWindow):
#     def __init__(self, controller):
#         super().__init__()
#         uic.loadUi("App Mixue/ui/admin_ui.ui", self)
#         self.setWindowTitle("Admin")
#         self.controller = controller

#         self.load_data_from_json()
    
#     def load_data_from_json(self):
#         try:
#             with open("accounts.json", "r", encoding="utf-8") as file:
#                 self.data = json.load(file)
#                 self.tableWidget.setRowCount(len(self.data))
#                 for row, item in enumerate(self.data):
#                     self.tableWidget.setItem(row, 0, QTableWidgetItem(item["username"]))
#                     self.tableWidget.setItem(row, 1, QTableWidgetItem(item["password"]))
#         except (FileNotFoundError, json.JSONDecodeError):
#             QMessageBox.warning(self, "Lỗi", "Không thể đọc file JSON!")


    
        



# class Controller:
#     def __init__(self):
#         self.admin_window = None


#     def show_login(self):
#         if self.signup_window:
#             self.signup_window.close()
#         self.login_window = Login(self)
#         self.login_window.show()

#     def show_signup(self):
#         if self.login_window:
#             self.login_window.close()
#         self.signup_window = SignUp(self)
#         self.signup_window.show()




# if __name__ == "__main__":
#     app = QApplication(sys.argv)

#     # Đặt style "Fusion" để kiểm soát giao diện
#     app.setStyle('Fusion')

#     # Tạo palette sáng
#     palette = QPalette()
#     palette.setColor(QPalette.ColorRole.Window, QColor(255, 255, 255))  # Màu nền trắng
#     palette.setColor(QPalette.ColorRole.WindowText, QColor(0, 0, 0))  # Màu chữ đen
#     palette.setColor(QPalette.ColorRole.Base, QColor(240, 240, 240))  # Màu nền cho ô nhập liệu
#     palette.setColor(QPalette.ColorRole.Text, QColor(0, 0, 0))  # Màu chữ trong ô nhập liệu
#     palette.setColor(QPalette.ColorRole.Button, QColor(255, 255, 255))  # Nền nút
#     palette.setColor(QPalette.ColorRole.ButtonText, QColor(0, 0, 0))  # Màu chữ nút
#     app.setPalette(palette)

#     # Tạo controller để quản lý màn hình
#     controller = Controller()
#     controller.show_login()

#     sys.exit(app.exec())