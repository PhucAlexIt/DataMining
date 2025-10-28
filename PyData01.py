import pandas as pd

data = pd.read_excel('./Data/data01.xlsx')
df = pd.DataFrame(data)
# print(df)
df["Rời rạc hóa: Chia điểm thành 3 phần (bins)"] = pd.cut(df["Tuổi"], bins=4, right=False)
print(df)