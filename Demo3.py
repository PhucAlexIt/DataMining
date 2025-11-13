import sklearn
import pandas as pd

df = pd.read_csv('./Files/Groceries_dataset.csv')
# print(df.head())
# print(df.isna().sum())
# print(df.isnull().sum())
for i in df.columns:
    missing_value = df[i].isna().sum()
    missing_percent = missing_value/len(df) * 100
    print(f"{i} bị thiếu là {missing_percent}")
