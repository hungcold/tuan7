import numpy as np

x = np.array([[14, 96],
              [46, 82],
              [80, 67],
              [77, 91],
              [99, 87]])
print("X = ", x)
print("Giá trị lớn nhất: ", np.amax(x))
print("Giá trị bé nhất: ", np.amin(x))
print("Giá trị lớn nhất (axis = 0): ", np.amax(x, axis=0))
print("Giá trị lớn nhất (axis = 1): ", np.amax(x, axis=1))

#bỏ qua phần tử nan
x = np.array([[14, 96],
              [np.nan, 82],
              [80, 67],
              [77, np.nan],
              [99, 87]])

print("X = ", x)
print("Bỏ qua giá trị nan")
print("Giá trị lớn nhất: ", np.nanmax(x))
print("Giá trị bé nhất: ", np.nanmin(x))

#phạm vi giá trị(range)
print("x = ", x)

print("Range = ", np.ptp(x))
print("Range (axis = 0) = ", np.ptp(x, axis=0))
print("Range (axis = 1) = ", np.ptp(x, axis=1))

#Bách phân vị (Percentiles) và Tứ phân vị (Quartiles)
scores = np.array([8, 6, 4, 3, 9, 4, 7, 4, 4, 9, 7, 3, 9, 4, 2, 3, 8, 5, 9, 6])
print("List",scores)
#interpolation là một phép nội quy, default là linear  tham số tùy chọn này chỉ định phương pháp nội suy để sử dụng khi phân vị mong muốn nằm giữa hai điểm dữ liệu i và j
#Có 5 kiểu nội suy NumPy hỗ trợ:
# ​'linear' (nội suy tuyến tính): i + (j - i) * fraction với fraction là phần phân số của chỉ số được bao quanh bởi i và j
# 'lower': i
# 'higher': j
# 'nearest': i hoặc j (chọn cái nào gần hơn)
# 'midpoint': (i + j) / 2
print("Bách phân vị thứ 70: ", np.percentile(scores, 70, interpolation='lower'))
print("Bách phân vị thứ 70: ", np.percentile(scores, 70, interpolation='higher'))
print("Bách phân vị thứ 70: ", np.percentile(scores, 70, interpolation='linear'))
print("Bách phân vị thứ 70: ", np.percentile(scores, 70, interpolation='nearest'))
print("Bách phân vị thứ 70: ", np.percentile(scores, 70, interpolation='midpoint'))
#khái niệm về trung vị (median) đã nói ở trên: trung vị là giá trị giữa của dãy số được sắp xếp từ bé đến lớn, vì vậy bách phân vị thứ 50 chính là median của dãy số đó
print("Bách phân vị thứ 50: ", np.percentile(scores, 50))
print("Median = ", np.median(scores))
print("Tứ phân")
print("Q1 = : ", np.quantile(scores, 0.25))
print("Q2 = : ", np.quantile(scores, 0.5))
print("Q3 = : ", np.quantile(scores, 0.75))