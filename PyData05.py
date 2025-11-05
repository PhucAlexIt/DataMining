import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import CategoricalNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = pd.read_excel("./Files/Data06a.xlsx")
df = pd.DataFrame(data)
df['Kẹt_xe'] = df['Kẹt_xe'].map({'Có':True,'Không':False})
data_encoding = LabelEncoder()
for i in ["Mưa",'Cuối_tuần','Buổi']:
    df[i] = data_encoding.fit_transform(df[i])

x = df[['Mưa','Cuối_tuần','Buổi']]
y = df['Kẹt_xe']

x_train, x_test , y_train, y_test = train_test_split(x,y, test_size=3, random_state=0)
model = CategoricalNB()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
# y_pred = model.predict(x_test)
# print(f"Dự đoán: {y_pred}")
# print(f"Thực tế: {y_test}")
