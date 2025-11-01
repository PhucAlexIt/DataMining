import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
df = pd.read_excel("./Files/data04.xlsx")
# print(df)
df["Diem"] = pd.cut(df["Diem"], bins= 3, right= True, labels=['Yếu','Khá','Giỏi'])
# print(df)
df_binary = pd.get_dummies(df).fillna(0).astype(int)
print(df_binary)