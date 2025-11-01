import pandas as pd
df = pd.read_excel('./Files/data03.xlsx')
Q1_age = df['Tuổi'].quantile(0.25)
Q3_age = df['Tuổi'].quantile(0.75)
IQR_age = Q3_age - Q1_age

Q1_salary = df['Lương (Triệu đồng)'].quantile(0.25)
Q3_salary = df['Lương (Triệu đồng)'].quantile(0.75)
IQR_salary = Q3_salary - Q1_salary
outlier_age = ((df['Tuổi'] < (Q1_age - 1.5 * IQR_age)) | (df['Tuổi'] > (Q3_age + 1.5 * IQR_age)))
outlier_salary = ((df['Lương (Triệu đồng)'] < (Q1_salary -1.5 * IQR_salary)) | (df['Lương (Triệu đồng)'] > (Q3_salary + 1.5 * IQR_salary)))
df['Phát hiện outliers'] = outlier_age | outlier_salary
print(df)
