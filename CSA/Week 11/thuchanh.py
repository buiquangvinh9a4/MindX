import pandas as pd

df = pd.read_excel('D:\Programming\MindX\CSA\Week 11\\provinces.xls')
print(df)

# lấy ra Population tại dòng 0
x = df.loc[0, 'Population']
print(x)
# lấy ra Area tại dòng 0
y = df.loc[0, 'Area']
print(y)

z = x / y * 1000
print(round(z, 6))

list = []   # khởi tạo list rỗng để lưu giá trị
for i in range(0, len(df)):  # chạy từ 0 đến 63
    x = df.loc[i, 'Population']   # lấy ra ô [i, 'Population']
    y = df.loc[i, 'Area']         # lấy ra ô [i, 'Area']
    z = x / y * 1000              # tính theo công thức
    list.append(round(z, 6))      # thêm vào list

print(list)         # in ra list vừa tạo
df['PopulationDensity'] = list   # thêm cột với tên là PopulationDensity và data là list
print(df)

# cần lấy ra giá trị max của mật độ dân số (Population Density)
maxPD = df['PopulationDensity'].max()
print(maxPD)

result = df[df['PopulationDensity'] == maxPD]
print(result)






# list_density = []

# for i in range(0, len(df)):
#     x = df.loc[i, 'Population'] / df.loc[i, 'Area'] * 1000
#     list_density.append(round(x, 6))
    
# df['PopulationDensity'] = list_density
# print(df)
