from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QListWidgetItem, QMessageBox
)
from PyQt6.QtCore import pyqtSignal   # gửi tín hiệu 
from PyQt6.QtGui import QPixmap
from PyQt6.uic import loadUi
import sys
import json

gioHang = []


class ProductItem(QWidget):
    def __init__(self, name, price, image, parent=None):
        super().__init__(parent)
        loadUi("ui/item.ui", self)  # Load file UI
        
        self.item_name.setText(name)
        self.item_price.setText(str(price) + " VNĐ")

        pixmap = QPixmap(image)
        self.item_image.setPixmap(pixmap.scaled(183, 115)) 

        self.item_buy.clicked.connect(lambda: self.them(name, price, image))

    
    def them(self, name, price, image):
        soLuong = self.item_quantity.value()
        if soLuong == 0:
            return 
        item = {
            "tenMatHang": name,
            "soLuong": soLuong,
            "giaTien": price * soLuong,
            "hinhAnh": image
        }

        isExist = False
        for it in gioHang:
            if it["tenMatHang"] == name:
                it["soLuong"] += soLuong
                it["giaTien"] += (price * soLuong)
                isExist = True
                break
        
        if not isExist:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setText("Đã thêm thành công " + str(soLuong) + " " + name)
            msg.setWindowTitle("Thông báo")
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)

            msg.exec()
            gioHang.append(item)
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setText("Đã cập nhật thành công " + str(soLuong) + " " + name)
            msg.setWindowTitle("Thông báo")
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        print(gioHang)


class PurchaseItem(QWidget):
    item_deleted = pyqtSignal()  # Tín hiệu phát ra khi xóa item

    def __init__(self, name, price, quantity, image, parent=None):
        super().__init__(parent)
        loadUi("ui/itemGioHang.ui", self)  # Load file UI
        
        self.item_name.setText(name)
        self.item_price.setText(str(price) + " VNĐ")
        self.item_quantity.setText("Số lượng: " + str(quantity))

        pixmap = QPixmap(image)
        self.item_image.setPixmap(pixmap.scaled(183, 115)) 
        
        
        self.btn_delete.clicked.connect(self.xoa)
    
    def xoa(self):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Xác nhận xoá")
        msg_box.setText(f"Bạn có chắc chắn muốn xoá {self.item_name.text()} khỏi giỏ hàng?")
        msg_box.setIcon(QMessageBox.Icon.Question)
        msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        # Đổi màu chữ thành đen
        msg_box.setStyleSheet("""
            QLabel { color: black; }
            QPushButton { color: black; }
        """)

        reply = msg_box.exec()

        if reply == QMessageBox.StandardButton.Yes:
            global gioHang
            gioHangNew = []
            for it in gioHang:
                if it["tenMatHang"] != self.item_name.text():
                    gioHangNew.append(it)
            gioHang = gioHangNew
            print(gioHang)

            self.item_deleted.emit()  # Gửi tín hiệu để cập nhật danh sách
            self.close()

        
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("ui/list.ui", self)  # Load file UI
        
        with open("db/userLogin.json", "r") as f:
            data = json.load(f)
            self.label_email.setText(data.get("email")) 

        self.openHome()
        self.btn_cart.clicked.connect(self.moLichSu)

        self.btn_history.clicked.connect(self.xemDatHang)


    def openHome(self):
        with open("db/items.json", "r") as f:
            data = json.load(f)
            print(data)
            lst_item = data
            print(len(lst_item))
        for i in range(len(lst_item)):
            name = lst_item[i]["tenMatHang"]
            price = lst_item[i]["giaTien"]
            image = lst_item[i]["hinhAnh"]
            product_item = ProductItem(name, price, image)

            item = QListWidgetItem(self.list_widget)
            item.setSizeHint(product_item.sizeHint())

            self.list_widget.addItem(item)
            self.list_widget.setItemWidget(item, product_item)

    def moLichSu(self):
        self.mo_lich_su = PurchaseHistory(self)
        self.mo_lich_su.show()

    def xemDatHang(self):
        pass
        # with open("db/purchase.json", "r") as f:
        #     data = json.load(f)
            
        #     for item in data:
        #         if item["username"] == self.label_email.text():
        #             pass


class PurchaseHistory(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("ui/purchase.ui", self)  # Load file UI
        
        self.tongSoTien = 0
        self.lb_tongSoTien.setText("0 VNĐ")
        self.email = ""

        with open("db/userLogin.json", "r") as f:
            data = json.load(f)
            self.email = data.get("email", "Không có email")
            print(self.email)
        
        
        self.capNhatGioHang()
        self.btn_thanhToan.clicked.connect(self.thanhToan)
        

    def capNhatGioHang(self):
        self.list_widget.clear()  # Xoá toàn bộ danh sách cũ
        self.tongSoTien = 0  # Reset tổng số tiền    
        self.lb_tongSoTien.setText("0 VNĐ") 
        for it in gioHang:
            name = it["tenMatHang"]
            quantity = it["soLuong"]
            price = it["giaTien"]
            image = it["hinhAnh"]
            
            product_item = PurchaseItem(name, price, quantity, image)
            product_item.item_deleted.connect(self.capNhatGioHang)

            item = QListWidgetItem(self.list_widget)
            item.setSizeHint(product_item.sizeHint())

            self.list_widget.addItem(item)
            self.list_widget.setItemWidget(item, product_item)
            
            self.tongSoTien += price
            self.lb_tongSoTien.setText(str(self.tongSoTien) + " VNĐ")

    def thanhToan(self):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Xác nhận đặt hàng")
        msg_box.setText(f"Bạn có chắc chắn muốn đặt hàng không? Hãy kiểm tra lại thông tin!")
        msg_box.setIcon(QMessageBox.Icon.Question)
        msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | 
                                   QMessageBox.StandardButton.No)

        # Đổi màu chữ thành đen
        msg_box.setStyleSheet("""
            QLabel { color: black; }
            QPushButton { color: black; }
        """)

        reply = msg_box.exec()

        if reply == QMessageBox.StandardButton.Yes:
            # thông báo 
            msg_ok = QMessageBox()
            msg_ok.setIcon(QMessageBox.Icon.Information)
            msg_ok.setText("Đã đặt hàng thành công. Vui lòng xem trong giỏ hàng.")
            msg_ok.setWindowTitle("Thông báo")
            msg_ok.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg_ok.exec()


            # ghi json vào purchase.json
            with open("db/purchase.json", "r", encoding="utf-8") as f:
                data = json.load(f)

                if type(data) == dict and len(data) == 0:
                    data = []
                
                from datetime import datetime
                dic = {
                    "username" : self.email,
                    "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "purchase" : gioHang
                }
                data.append(dic)
                with open("db/purchase.json", "w") as f:
                        json.dump(data, f, indent = 4, ensure_ascii=False)
            self.close()





app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())