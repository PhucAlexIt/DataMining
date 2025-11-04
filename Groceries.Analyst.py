import pandas as pd
from mlxtend import frequent_patterns
df = pd.read_csv("./Files/Groceries_dataset.csv")
df.drop(columns=["Date"], inplace=True)
# print(df.info())
df = df.dropna()
tongTrungLap = df.duplicated().sum()
df.drop_duplicates(inplace=True)
# Transaction list
# transaction = df.groupby("Member_number")["itemDescription"].apply(list)
# print(transaction.head)
df_transaction = pd.crosstab(df["Member_number"],df["itemDescription"])
# print(df_transaction.head())
fq_a = frequent_patterns.apriori(df_transaction, min_support=0.01, use_colnames=True)
fq_a = fq_a.sort_values(by="support", ascending=False)
# print(fq_a.head())
fq_rules = frequent_patterns.association_rules(fq_a, min_threshold= 0.5, metric="lift")
fq_rules = fq_rules.sort_values(by="confidence", ascending=False)
strong_fq_rules = fq_rules[(fq_rules['confidence'] > 0.6) & (fq_rules["lift"] > 1.2)]
print(strong_fq_rules[["confidence",'lift','support']])
# print(df) 
