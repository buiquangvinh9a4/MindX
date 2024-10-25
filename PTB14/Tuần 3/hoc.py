diemToiDa = 10
diemCuaBan = 0

cau1 = int(input("Câu 1: 1 + 1 = "))
if cau1 == 2:
    print("Câu trả lời đúng.")
    diemCuaBan += 1
else:
    print("Bạn còn hơi kém.")

cau2 = input("Câu 2: Mặt trời mọc ở đằng nào? Trả lời: ")
if cau2 == "Đông":
    print("Kiến thức địa lý của bạn tốt đấy.")
    diemCuaBan += 1
else:
    print("Bạn còn chưa hiểu về vũ trụ.")

print("=== Kết quả: ", diemCuaBan, "/", diemToiDa)