import numpy as np

coins = np.random.randint(2, size=1000)
print(coins.shape)
print("% số lần tung được mặt ngửa: ", (coins == 0).mean() * 100)
print("% số lần tung được mặt úp: ", (coins == 1).mean() * 100)

# ví dụ ta muốn số mặt úp đạt 80% còn số mặt ngửa chỉ 20%
coins = np.random.choice([0, 1], size=1000, p=[0.2, 0.8]) # random.choice sẽ lấy ngẫu nhiên các phần tử trong mảng ở tham số đầu tiên với xác suất ở tham số p
print("% số lần tung được mặt ngửa: ", (coins == 0).mean() * 100)
print("% số lần tung được mặt úp: ", (coins == 1).mean() * 100)

np.random.binomial(20, 0.5) # Số mặt ngửa nhận được khi tung đồng xu 10 lần
np.random.binomial(20, 0.5, 10) # Số mặt ngửa nhận được khi tung đồng xu 20 lần trong 10 lần lặp
print("Trung bình số mặt ngửa nhận được khi tung đồng xu 20 lần trong vòng 10 lần lặp: ", np.random.binomial(20, 0.5, 10).mean())

# Ở 2 trường hợp trên, dễ thấy ta đang dùng đồng xu không bị thiên vị (p=0.5) nên mới có được 10.4 mặt ngửa sau 20 lần tung (tương đương 50%).
# Ta có thể thêm bias vào như sau
n = 10  # tung 10 đồng xu trong 1 lần
p = 0.2  # bias cho mặt ngửa (xác suất cho mặt ngửa là 0.2)
l = 1000  # số lần lặp

b = np.random.binomial(n, p, l)
print("Trung bình số mặt ngửa nhận được: ", b.mean())