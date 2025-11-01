import pandas as pd


df = pd.read_excel("./Files/Bank.xlsx")
# Kiểm tra dl bị trùng lặp
# print(df.duplicated().sum())
# print(df.duplicated().any())


df.drop(columns=['CustomerId', 'Name'], inplace=True)
# print(df.info())
# Kiểm tra dl bị thiếu
# print(df.isnull().sum())

df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
df['Age'].fillna(df['Age'].mean(), inplace=True)
print(df.info())

# print(df.isna().sum())

