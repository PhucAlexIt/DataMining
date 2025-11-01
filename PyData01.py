import pandas as pd

data = pd.read_excel('./Files/data01.xlsx')
df = pd.DataFrame(data)
df["Rời rạc hóa: Chia điểm thành 3 phần (bins)"] = pd.cut(df["Tuổi"], bins=3, right=False, labels=['Trẻ','Trưởng thành','Già'])
print(df)