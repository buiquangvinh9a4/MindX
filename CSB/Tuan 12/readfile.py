# vanban = open('vanban.txt', 'r')  # mở file

# for line in vanban:      # duyệt từng dòng của file
#     print(line)

# vanban.close()  # đóng file 

dic_name = {}       # từ điển chứa họ tên và điểm

with open('vanban.txt', 'r') as vanban:
    for line in vanban:
        line = line.replace('\n', '')  # loại bỏ dấu xuống dòng
        index = line.rfind(' ')      # tìm vị trí dấu cách cuối cùng
        
        name = line[:index]            # tách tên
        score = float(line[index + 1:])   # tách điểm
        dic_name.update({name: score})  # thêm vào dic_name

max_score = max(dic_name.values())   # tìm ra giá trị điểm lớn nhất

for name, score in dic_name.items():
    if score == max_score:   # so sánh điểm của từng HS với điểm lớn nhất
        print(name)           # bằng nhau -> In ra màn hình
        