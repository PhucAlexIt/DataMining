import pandas as pd

# data = {"Name":["Nhã Quỳnh","Hải","Ngô"], "Age":[17, 12, 17], "Gpa": [2.78, 2.5, 3.3]}
# data = pd.DataFrame(data)
# data['is_Active'] = [True, False, False]
# new_row = pd.DataFrame([{"Name": "Trinh", "Age":20, "Gpa":1.7},
#                         {"Name": "Siu", "Age":10, "Gpa": 2.2, "is_Active":True}])
# data = pd.concat([new_row, data])
# print(data.loc[1])
# df = pd.read_csv("./Files/Groceries_dataset.csv", index_col=["Member_number"])
# df = pd.read_csv("./Files/Groceries_dataset.csv")
# favour_item = df[(df['itemDescription'] == "whole milk") & (df['Member_number'] > 4000)]
# favour_item = df[(df['itemDescription'] == "whole milk") | (df['Member_number'] < 2000)]
# print(favour_item)
# print(df.min(numeric_only=True))
# print(df.max(numeric_only=True))
# print(df.count())
# g = df.groupby("Member_number")
# print(g['itemDescription'].count())
# print(g['itemDescription'].sum())
# print(df.columns) 
# print(df[['itemDescription','Member_number']])
# print(df.loc[3037,['itemDescription']])
# print(df.iloc[0:5, 0:2])
# print(df)
