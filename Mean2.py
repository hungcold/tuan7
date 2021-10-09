import numpy as np

X = np.array([2, 5, 3, 1, 7])
Y = np.array([2, 1, 8, 5, 7, 9])

list_x = sorted(X)
list_y = sorted(Y)
print("Sắp xếp X", list_x)
print("Sắp xếp Y", list_y)

print("Tính median X = ", np.median(X))
print("Tính median Y = ", np.median(Y))

arr = np.array([[7, 4, 2], [3, 9, 5]])
print("list cần tính",arr)
print("Tính median arr (axis = 0) = ", np.median(arr, axis=0))
print("Tính median arr (axis = 1) = ", np.median(arr, axis=1))

freetuts_visitors = np.array([3776, 3112, 3476, 3319, 3559, 2121, 3462])
print("List",freetuts_visitors)
print("Số người truy cập trung bình mỗi ngày trong tuần qua của Freetuts: ", np.mean(freetuts_visitors))

freetuts_visitors = np.array([3776, 3112, 3476, 3319, 3559, 50293, 30432]) # 2 giá trị cuối lệch xa so với các giá trị trong dãy
print("List:",freetuts_visitors)
print("Mean = : ", np.mean(freetuts_visitors))
print("Median = : ", np.median(freetuts_visitors)) #median cho giá trị biểu thị tốt hơn

x = np.array([2, np.nan, 5, 9])#bỏ qua phần tử nan khi tính mean và median
print("List",x)
print("mean = ", np.nanmean(x))
print("median = ", np.nanmedian(x))
print("nếu dùng lệnh mean và media sẽ như sau")
print("mean = ", np.mean(x))
print("median = ", np.median(x))

