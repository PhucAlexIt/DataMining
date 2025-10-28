import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
from mlxtend.frequent_patterns import apriori, association_rules

data = pd.read_csv('./File/Groceries_dataset.csv')
data = data.drop(columns=['Date'])

data = data.dropna()
data = data.drop_duplicates()
df_data = pd.DataFrame(data)
data = pd.crosstab(df_data['Member_number'], df_data['itemDescription'])
fq = apriori(data, min_support=0.15, use_colnames=True)
rules = association_rules(fq,  metric='confidence', min_threshold=0.5)
print(rules[['support', 'confidence','lift']])
