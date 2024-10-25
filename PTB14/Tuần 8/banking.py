import os    # chứa lệnh xoá màn hình
import datetime   # chứa lệnh truy vấn thời gian

sodu = 50000   # số dư tài khoản mặc định
thoiGianNap = []   # khai báo danh sách rỗng chứa thời gian nạp

os.system('clear')   # xoá màn hình

while True:
    print("==== QUANG VINH BANK ====")
    print("0. Xem số dư")
    print("1. Nạp tiền")
    print("2. Rút tiền")
    print("3. Xem lịch sử nạp tiền")
    print("4. Xem lịch sử rút tiền")
    print("5. Thoát")

    choice = int(input("--> Lựa chọn của bạn: "))

    if choice == 0:
        print("Số dư hiện tại:", sodu, "VNĐ") 

    elif choice == 1:
        os.system('clear')
        print("=== NẠP TIỀN ===")
        nap = int(input("Số tiền cần nạp: "))
        sodu += nap   # cộng số tiền nap  vào số dư

        thoiGian = datetime.datetime.now()  # lấy thời gian khi nạp
        thoiGianNap.append(thoiGian)  # đẩy thời gian vào list

        print("Bạn đã nạp thành công", nap, "VNĐ")
        print("Số dư hiện tại:", sodu, "VNĐ")

    elif choice == 2:
        os.system('clear')
        print("=== RÚT TIỀN ===")
        rut = int(input("Số tiền muốn rút: "))

        if rut > sodu:
            print("Tài khoản của bạn không đủ số dư")
        else:
            sodu -= rut   # trừ số tiền rút ra khỏi số dư
            print("Bạn đã rút thành công ", rut, "VNĐ")
            print("Số dư hiện tại: ", sodu, "VNĐ")

    elif choice == 3:
        os.system('clear')
        print("=== LỊCH SỬ NẠP TIỀN ===")
        for thoiGian in thoiGianNap:
            print("-", thoiGian)

    elif choice == 4:
        pass
    elif choice == 5:
        print("Cảm ơn bạn đã sử dụng dịch vụ!")
        break

