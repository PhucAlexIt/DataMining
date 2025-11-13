import pandas as pd

df = pd.read_csv("./Files/Groceries_dataset.csv")
df = df.drop(columns=['Date'])
# sum_df = df.isnull().count()
# print(sum_df)
# print(df.info())
df = df.dropna()
# df =df.fillna(df.median(numeric_only=True))
df = df.drop_duplicates()
print(df)
