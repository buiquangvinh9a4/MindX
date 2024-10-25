
import pandas as pd

data = pd.read_excel('D:\Programming\MindX\CSA\Week 10\\data.xlsx')
data.columns = ['STT', 'Mã SV', 'Họ tên', 'Ngày sinh', 'Lớp', 'Đăng kí tổ BM', 'GVHD', 'Đồng GVHD']

print(data)

list_students = []
list_teachers = []

for i in range(1, len(data)):
    list_students.append(data.loc[i, 'Họ tên'])
    if data.loc[i, 'GVHD'] not in list_teachers:
        list_teachers.append(data.loc[i, 'GVHD'])


print(list_students)
print(list_teachers)