import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_excel('D:\Programming\MindX\CSA\Week 12\provinces.xls')
# print(data)



X = data.loc[:, ['Region', 'Area']]
print(X)

Regions = []

for region in data.loc[:, 'Region']:
    if region not in Regions:
        Regions.append(region)

Areas = []

for region in Regions:
    tmp = data.loc[data['Region'] == region, 'Area'].sum()
    Areas.append(tmp)
  


# for region in Regions:
#     sum = 0
#     for i in range(len(data)):
#         if data.loc[i, 'Region'] == region:
#             sum += data.loc[i, 'Area']
#     Areas.append(round(sum, 2))

plt.figure(figsize=(16, 7))
plt.bar(Regions, Areas)
# plt.plot(Regions, Areas, 'r')
plt.show()

    
# print(X)
# print(Y)