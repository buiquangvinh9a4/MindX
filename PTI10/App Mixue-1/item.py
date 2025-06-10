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
            gioHang = [item for item in gioHang if item["tenMatHang"] != self.item_name.text()]
            print("Giỏ hàng sau khi xóa:", gioHang)

            self.item_deleted.emit()  # Gửi tín hiệu để cập nhật danh sách
            self.close()

    

        
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("ui/list.ui", self)  # Load file UI
        self.btn_cart.clicked.connect(self.moLichSu)




        self.openHome()
        self.resetJson()
        

    
    def resetJson(self):
        # Xoá nội dung bằng cách ghi một đối tượng JSON rỗng
        with open("db/purchase.json", "w") as file:
            json.dump({}, file) 

    def openHome(self):
        lst_item = []
        with open("db/items.json", "r") as f:
            data = json.load(f)
            lst_item = data
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


class PurchaseHistory(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("ui/purchase.ui", self)  # Load file UI
        self.tongSoTien = 0
        self.edt_tongSoTien.setText("0 VNĐ")
        self.capNhatGioHang()
            

    def capNhatGioHang(self):
        self.list_widget.clear()  # Xoá toàn bộ danh sách cũ
        self.tongSoTien = 0  # Reset tổng số tiền    
        self.edt_tongSoTien.setText("0 VNĐ") 
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
            self.edt_tongSoTien.setText(str(self.tongSoTien) + " VNĐ")
            

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())