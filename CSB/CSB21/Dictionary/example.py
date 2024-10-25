import os
os.system("clear")

# data của cửa hàng
kho = {
    "Iphone 15 Pro Max": 29990000,
    "Macbook Pro M4 14inch": 54000000
}

def menu():
    print("========== Hệ thống quản lý hàng ========")
    print("1. Xem danh sách sản phẩm")
    print("2. Thêm sản phẩm")
    print("3. Tìm kiếm sản phẩm")
    print("4. Sửa thông tin sản phẩm")
    print("5. Xóa sản phẩm")
    print("6. Thoát chương trình")
    print("=" * 50)

def menu_1():
    print("========== Danh sách sản phẩm ========")
    i = 1
    for key, value in kho.items():
        print(f"{i}. {key}: {value} VND")
        i += 1
    luachon = input("Bấm 0 để quay lại: ")
    while True:
        if luachon == "0":
            menu()
            break
        else:
            luachon = input("Lựa chọn sai, vui lòng nhập lại:  ")

menu()
while True:
    luaChon = int(input("Lựa chọn của bạn: "))
    if luaChon == 1:
        menu_1()
    if luaChon == 6:
        print("See u again!")
        break


