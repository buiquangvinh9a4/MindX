import matplotlib.pyplot as plt

# Dữ liệu ví dụ
labels = ['Quả táo', 'Quả cam', 'Quả lê', 'Quả xoài']
sizes = [15, 30, 45, 10]

# Tạo biểu đồ tròn
plt.pie(sizes, labels=labels)
plt.legend(loc="upper right")
# Hiển thị biểu đồ
plt.show()