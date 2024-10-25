import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('D:\Programming\MindX\CSA\Week 12\covid19.csv')


data_new = data.iloc[:, [1, 2, 3, 6, 7]]
# print(data_new.loc[data_new['confirmed'] < 5000])

lst_country = data_new['Country/Region'].unique()
lst_country_loc = ['Tajikistan', 'Vietnam', 'Thailand', 'Yemen', 'Malaysia', 'Japan']
lst_confirmed = []

for country in lst_country_loc:
    
    sum = data_new.loc[data_new['Country/Region'] == country, 'confirmed'].sum()
    lst_confirmed.append(sum)
    
print(data_new[['Country/Region','confirmed']])

plt.figure(figsize=(15,6))
plt.bar(lst_country_loc, lst_confirmed)
plt.bar(lst_country_loc[5], lst_confirmed[5], color='yellow')
plt.suptitle('Biểu đồ hiển thị số người nhiễm Covid 19 2021', fontsize= 16)
plt.xlabel('Country', fontsize=16)
plt.ylabel('Death', fontsize=16)
plt.show()

