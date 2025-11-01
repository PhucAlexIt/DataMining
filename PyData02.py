import pandas as pd

df = pd.read_excel("./Files/data02.xlsx")
df['Điểm_DM'] = pd.to_numeric(df['Điểm_DM'], errors='coerce')
df['Điền giá trị thiếu'] = df['Điểm_DM'].fillna(df['Điểm_DM'].median())
print(df)