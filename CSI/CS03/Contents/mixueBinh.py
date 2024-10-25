from collections import deque
import os

def menu():
    print("====MIXUE HDT====")
    print("1. Xem menu")
    print("2. Order")
    print("3. Xoa order")
    print("4. Thanh Toan")
    print("5. Thoat")


def menu_1():
    os.system("cls")
    print("===Menu tra sua===")
    i = 1
    for ten, gia in menuTS.items():
        print(f"- {i}: {ten}: {gia}")
        i += 1
    tmp = input("Bam phim bat ki de thoat")
    os.system("cls")


def menu_2():
    os.system("cls")
    print("===Your order=====")
    trasua = input("Nhap tra sua ban muon order: ")
    a = trasua
    if trasua.title() in menuTS:
        orders.append(trasua)
        print(f"Order {a} da them thanh cong!")
        tmp = input("Nhan phim bat ki de thoat")
        os.system("cls")
    else: 
        print("Tra sua ban chon khong co trong menu!")
        tmp = input("Nhan phim bat ki de thoat")
        os.system("cls")

def menu_3():
    os.system("cls")
    trasuaxoa = orders.pop()
    print(f"Order {trasuaxoa.title()} da xoa thanh cong!")
    tmp = input("Nhan phim bat ki de thoat")
    os.system("cls")

menuTS = {
    "Tra Sua Tran Chau": 25000,
    "Tra Chanh":10000,
    "Tra Chanh Xanh": 15000,
    "Tra Cam": 12000,
}


orders = deque()

os.system("cls")
while True:
    menu()
    choice = int(input("----> Nhap vao lua chon cua ban "))

    if choice == 1:
        menu_1()
    if choice == 2:
        menu_2()