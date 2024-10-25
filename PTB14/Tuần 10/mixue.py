import os 
dsTraSua = ["Trà chanh Lô Hội",
            "Sữa chua Trân châu Đường đen",
            "Trà sữa Bạc hà",
            "Trà sữa Than tre"]
dsGiaTien = [17000, 25000, 20000, 30000]

dsOrder = []
tienTra = 0


def menuMixue():
    print("=== MIXUE HOÀNG ĐẠO THUÝ XIN CHÀO ===")
    print("1. Xem danh sách trà sữa.")
    print("2. Thêm trà sữa.")
    print("3. Xoá trà sữa.")
    print("4. Thanh toán.")
    print("5. Thoát.")
    print("=====================================")

def menu1():
    os.system("clear")
    print("Cửa hàng chúng tôi có: ")
    for i in range(len(dsTraSua)):
        print(i + 1, ".", dsTraSua[i], "-", dsGiaTien[i])

    print("*********************")

def menu2(tienTra):
    os.system("clear")
    viTri = int(input("Bạn muốn thêm trà sữa số mấy: "))
    if viTri > len(dsTraSua):
        print("Chúng tôi không có trà sữa này.")
    else:
        dsOrder.append(dsTraSua[viTri - 1])
        tienTra = tienTra + dsGiaTien[viTri - 1]
        print("Bạn đã Order thành công", dsTraSua[viTri - 1])
        
    return tienTra

def menu3(tienTra):
    os.system("clear")
    for i in range(len(dsOrder)):
        print(i + 1, ".", dsOrder[i])
    
    viTri = int(input("Nhập STT trà sữa muốn xóa: "))

    if viTri <= len(dsOrder):
        traSuaXoa = dsOrder.pop(viTri - 1)
        viTriXoa = dsTraSua.index(traSuaXoa)
        tienTra = tienTra - dsGiaTien[viTriXoa]
        print("Bạn đã xóa", traSuaXoa)
    else:
        print("Không có trà sữa này.")

    return tienTra

def menu4(tienTra):
    os.system("clear")
    print("=== DANH SÁCH TRÀ SỮA BẠN ĐANG ORDER ===")
    for i in range(len(dsOrder)):
        print(i + 1, ".", dsOrder[i])
    print("--> Bạn phải trả số tiền là:", tienTra)

    ten = input("Nhập họ tên của bạn để thanh toán: ")

    thongBao1 = "Cảm ơn bạn " + ten.title()
    thongBao2 = "Bạn đã trả " + str(tienTra)

    print(thongBao1)
    print(thongBao2)

    dsOrder.clear()
    tienTra = 0
    print("*********************")

    return tienTra

os.system("clear")   # windows -> cls


while True:
    menuMixue()
    luaChon = int(input("--> Lựa chọn của bạn: "))

    if luaChon == 1:
        menu1()
    
    if luaChon == 2:
        tienTra = menu2(tienTra)

    elif luaChon == 3:
        tienTra = menu3(tienTra)

    elif luaChon == 4:
        tienTra = menu4(tienTra)

    elif luaChon == 5:
        print("!!! Cảm ơn đã sử dụng dịch vụ !!!")
        break


