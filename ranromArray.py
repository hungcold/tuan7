import numpy as np
#numpy.random.rand trả về một mảng các số ngẫu nhiên mà mỗi phần tử là một số ngẫu nhiên có phân bố đều (uniform distribution) trong khoảng [0, 1)
a = np.random.rand()
b = np.random.rand(4)  # Mảng có 1x8 phần tử
c = np.random.rand(2, 3)  # Mảng có 2x3 phần tử

print("a = ", a)
print("b = ", b)
print("c = ", c)

#NumPy không thực sự tạo ra số ngẫu nhiên mà thực chất nó sử dụng bộ sinh số giả ngẫu nhiên (Pseudorandom number generator)
#Hàm numpy.random.seed là một hàm tạo các bộ sinh số ngẫu nhiên (random generator) và tham số thường là một số nguyên không âm
#các giá trị của biến số khác nhau thì sẽ cho ra các số ngẫu nhiên khác nhau, và ngược lại, giống nhau thì sẽ ra số giống nhau, ví dụ
g = np.random
g.seed(10)

print("g rand: ", g.rand())

#numpy.random.normal
#Phân phối chuẩn, còn gọi là phân phối Gauss hay (Hình chuông Gauss), là một phân phối xác suất cực kì quan trọng trong nhiều lĩnh vực
#Nó là họ phân phối có dạng tổng quát giống nhau, chỉ khác tham số vị trí (giá trị trung bình μ - mean) và tỉ lệ (phương sai σ^2 - variance).
#Trong NumPy, ta có thể tạo ra một mảng dựa trên phân phối chuẩn bằng hàm random.normal có cú pháp:
np.random.normal(loc=0.0, scale=1.0, size=None) # loc = mean, scale = standard deviation
m, sigma = 0, 0.1 # mean và standard deviation
s = np.random.normal(m, sigma, size=5)
s

#numpy.random.randn#Đây cũng là một hàm sinh ra một mảng số tuân theo phân phối chuẩn, nhưng kết quả trả về là mảng có các phần tử phân bố theo phân phối chuẩn có mean = 0 và standard deviation = 1 (phân phối được chuẩn hoá)
#Hàm random.randn khá đơn giản, nó chỉ nhận duy nhất các tham số là một dãy số tương ứng với số chiều của mảng, chẳng hạn
np.random.randn(3, 3)
#Vì là phân phối được chuẩn hoá nên ta có thể sử dụng hàm này thay cho random.normal trên như sau:
# sigma * np.random.randn(...) + m

#numpy.random.uniform
#Hàm này sẽ sinh ra một mảng có giá trị phân phối đều (uniform distribution) trong một khoảng nhất định cho trước. Hàm có cú pháp như sau:
np.random.uniform(low=0.0, high=1.0, size=None)
#Để tạo một phân phối đều trong NumPy:
u = np.random.uniform(size=4)
print(u)

#numpy.random.permutation
#Mục đích của hàm chính là tạo nên một dãy hoán vị, chẳng hạn:
p = np.random.permutation(10)
print(p)