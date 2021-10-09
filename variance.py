import numpy as np

freetuts_ages = [19, 33, 51, 22, 18, 13, 45, 24, 58, 11, 25, 27, 26, 29]
print("List",freetuts_ages)
print("Phương sai: ", np.var(freetuts_ages))
print("Độ lệch chuẩn: ", np.std(freetuts_ages))

a = np.array([1, np.nan, 3, 4]) #xử lí nan
print("List",a)

print("var = ", np.var(a))
print("std = ", np.std(a))

print("Khi bỏ nan")#cũng như mean và media, numpy cung cho bỏ qua các phần tử nan trong list
print("nanvar = ", np.nanvar(a))
print("nanstd = ", np.nanstd(a))