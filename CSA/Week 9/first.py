import pandas as pd        # import thư viện pandas, đặt tên pd

# # list_students = ['Nguyên', 'Huy', 'Linh', 'Vi', 'Quân', 'Đức', 'Minh']
# # sr_students = pd.Series(list_students, [1, 2, 3, 4, 5, 6, 7])

# # print(sr_students)  # hiển thị sr_students ra ngoài màn hình

# import pandas as pd        # import thư viện pandas, đặt tên pd

# list_country = ['Việt Nam', 'Nhật Bản', 'Trung Quốc']
# list_city = ['Hà Nội', 'Tokyo', 'Bắc Kinh']
# sr_info = pd.Series(list_country, index = list_city, name = 'Thủ đô các nước')


# print(sr_info)


# list_numbers = {'Việt Nam': 'Hà Nội', 'Nhật Bản': 'Tokyo', 'Trung Quốc': 'Bắc Kinh', 'Pháp':'Paris'}
# sr_numbers = pd.Series(list_numbers, name = 'Thủ đô các nước a')

# # print(sr_numbers)


# # sr1 = pd.Series(['Vinh', 'Trang', 'Hiền'])
# # print(sr1)


# # # ví dụ 1: list chứa tên của các bạn học sinh lớp CSA12
# # list_name = ['Nguyên', 'Huy', 'Linh', 'Vi', 'Quân', 'Đức', 'Minh']

# # # ví dụ 2: list chứa điểm bài tập của các bạn học sinh lớp CSA12
# # list_score = [10, 9, 8.5, 7.5, 6.5, 5.5, 7]


# # vd1: dict1 lưu trữ key là tên, value là số điện thoại
# dict1 = {'Hải Nguyên' : 123456, 'Khánh Linh' : 987654}

# # vd2: dict2 lưu trữ key là mã tỉnh, value là tên tỉnh
# dict2 = {29: 'Hà Nội', 14: 'Quảng Ninh', 99: 'Bắc Ninh'}

# # dtframe = pd.DataFrame(dict2)
# # print(dtframe)



dict = {'số nguyên dương': pd.Series([1, 2, 3, 4, 5], index = ['a', 'b', 'c', 'd', 'e']),
         'số nguyên tố': pd.Series([2, 3, 5, 7, 11], index = ['a', 'b', 'c', 'd', 'e']),
         'số chính phương': pd.Series([1, 4, 9, 16, 25], index = ['a', 'b', 'c', 'd', 'e'])}

df = pd.DataFrame(dict)
print(df)
df.to_excel("D:\Programming\MindX\CSA\Week 9\\abc123.xlsx")

# tkb = {'Tiết': pd.Series([1, 2, 3, 4, 5], index = [1, 2, 3, 4, 5]),
#        'Thứ 2': pd.Series(['Toán', 'Toán', 'Văn', 'Hoá', 'Sử'], index = [1, 2, 3, 4, 5]),
#        'Thứ 3': pd.Series(['Toán', 'Tin', 'Anh', 'Địa', 'GDCD'], index = [1, 2, 3, 4, 5]),
#        'Thứ 4': pd.Series(['Văn', 'Văn', 'Thể dục', 'Sinh', 'Lý'], index = [1, 2, 3, 4, 5]),
#        'Thứ 5': pd.Series(['Lý', 'Văn', 'Văn', 'Tin', 'Anh'], index = [1, 2, 3, 4, 5]),
#        'Thứ 6': pd.Series(['Hóa', 'Thể dục', 'Toán', 'Sinh', 'Sinh hoạt'], index = [1, 2, 3, 4, 5]),}
# df = pd.DataFrame(tkb)






# file = pd.read_excel("D:\Programming\MindX\CSA\Week 9\\tkb.xlsx")
# print(file)

