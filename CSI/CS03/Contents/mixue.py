from collections import deque 
import os

def menu():
    print("==== MIXUE HOÀNG ĐẠO THUÝ ====")
    print("1. Xem menu trà sữa")
    print("2. Order trà sữa")
    print("3. Xoá trà sữa")
    print("4. Thanh toán")
    print("5. Thoát")

def menu_1():
    os.system("clear")
    print("==== MENU TRÀ SỮA ====")
    i = 1
    for ten, gia in menuTraSua.items():
        print(f"- {i}: {ten} - {gia} VND")
        i += 1
    tmp = input("Bấm phím bất kì để thoát....")
    os.system("clear")

def menu_2():
    os.system("clear")
    print("==== ORDER TRÀ SỮA ====")
    traSua = input("Nhập trà sữa bạn muốn Order: ")
    traSua = traSua.title()

    if traSua.title() in menuTraSua:
        orders.append(traSua)        # đẩy trà sữa vào ngăn xếp
        print("Đã order", traSua)
        tmp = input("Bấm phím bất kì để tiếp tục....")
        os.system("clear")
    else:
        print("Trà sữa không tồn tại")
        tmp = input("Bấm phím bất kì để tiếp tục....")
        os.system("clear")

def menu_3():
    os.system("clear")
    if len(orders) > 0:
        traSuaXoa = orders.pop()
        print("Bạn đã xoá", traSuaXoa)
        tmp = input("Bấm phím bất kì để tiếp tục....")
        os.system("clear")
    else:
        print("Bạn chưa order gì cả....")
        tmp = input("Bấm phím bất kì để tiếp tục....")
        os.system("clear")

def menu_4():
    print("===== MENU THANH TOÁN =====")
    thanhToan = 0
    i = 1
    while len(orders) > 0:
        traSua = orders.pop()
        giaTien = menuTraSua[traSua]
        print(f"{i}. {traSua} - {giaTien}")
        thanhToan += giaTien
        i += 1
    
    print(f"Thành tiền: {thanhToan} VND.")
    tmp = input("Bấm OK để thanh toán!")



menuTraSua = {           # menu trà sữa của cửa hàng
    "Trà Sữa Trân Châu": 25000,
    "Trà Chanh Lô Hội": 17000,
    "Trà Sữa Bạc Hà": 28000
}

orders = deque()   # list order trà sữa của khách hàng

os.system("clear")   # máy win: os.system("cls")  -> xoá màn hình
while True:
    menu()
    luaChon = int(input("--> Lựa chọn của bạn là: "))

    if luaChon == 1:
        menu_1()
    
    elif luaChon == 2:
        menu_2()

    elif luaChon == 3:
        menu_3()

    elif luaChon == 4:
        menu_4()

    elif luaChon == 5:
        print("Cảm ơn quý khách đã sử dụng dịch vụ!")
        break