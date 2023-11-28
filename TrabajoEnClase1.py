import pandas as pd

df_COVID = pd.read_csv("MinTIC2023/COVID clinical trials.csv")
df_COVID.info()

#Null values cleaning
df_COVID_cl1 = df_COVID.dropna()
df_COVID_cl1.info()

#Duplicated values cleaning
print(df_COVID_cl1.duplicated())
df_dup = df_COVID_cl1[df_COVID_cl1.duplicated()]
print(df_dup.info())
print(df_dup)
df_COVID_cl1.drop_duplicates(inplace=True)