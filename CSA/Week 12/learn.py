import matplotlib.pyplot as plt

# tạo biểu đồ đường (plot)  # trục x, trục y, nhãn, màu
plt.plot(['Vi', 'Linh', 'Huy', 'Minh'] , [8, 7, 9, 8])
plt.title('Biểu đồ Điểm của lớp CSA12', fontsize=17, color='red')

plt.xlabel('Học sinh')
plt.ylabel('Điểm')

plt.show()