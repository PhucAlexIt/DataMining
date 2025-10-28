import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


arr = np.array([3,7,8,9,15,20,21,22,23, 25,26,28,250])
s = pd.Series(arr)
print(s)
print('Giá trị trung vị: ',s.median())
print('Giá trị trung bình: ',s.mean())
print('Giá trị xuất hiện nhiều nhất: ',s.mode().tolist())
q1 = np.percentile(s, 25)
q2 = np.percentile(s, 50)
q3 = np.percentile(s, 75)
IQR = q3 - q1
print(q1)
print(q2)
print(q3)
print('Khoảng tứ phân vị: ',IQR)

st = s.std()
print('Giá trị độ lệch chuẩn: ',st)
low_val = q1 - 1.5 * IQR
high_val = q3 + 1.5 * IQR
print(low_val)
print(high_val)
outlier = s[(s >= low_val)&(s <= high_val)]
print("Loại outlier dùng mean: ", outlier.mean())
print("Loại outlier dùng std: ", outlier.std())

plt.figure(figsize=(8,8))
plt.boxplot(s)
plt.title('Phát hiện outlier')
plt.grid(True)
plt.show()
