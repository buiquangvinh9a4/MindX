import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('D:\Programming\MindX\CSA\Week 12\\pokemon_data.csv')

column = data.columns

print(data.loc[:, ['Name', 'Type 1', 'Type 2']])
print(data.loc[(data['Type 1'] == 'Poison') & (data['Type 2'] == 'Flying'), ['Name', 'Type 1', 'Type 2']])
type1 = data.loc[:, 'Type 1'].unique()
count_type1 = []

for type in type1:
    count_type1.append((data.loc[data['Type 1'] == type, 'Type 1']).count())
    
print(type1)

print(count_type1)

plt.figure(figsize=(13, 7))
# plt.pie(count_type1, labels = type1, autopct='%1.1f%%' )
plt.barh(type1, count_type1, labels = type1)

s = ''
for type in type1:
    s = s + str(type) + ', '
    
    
plt.title(s, fontsize=18)
plt.ylabel('Các hệ')
plt.xlabel('Số lượng')

i = 0
# type1: tên các hệ nhân vật: water, ground, fire,...
# count_type1:  đếm số lượng các hệ nhân vật: water có 5 con, ground có 10 con,....
for type in type1:
    plt.annotate(count_type1[i], xy=(count_type1[i] + 2, type), fontsize=9, color='red')
    i += 1
    # plt.annotate(giá trị cần ghi,  tọa độ cần ghi (x, y), ....)
    

plt.legend()
plt.savefig('pic.png')
plt.show()

print(count_type1[0])




