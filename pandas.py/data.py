import pandas as pd
data=pd.read_csv("C:\\Users\\Mohammed Mateen\\Desktop\\data.txt")
print(data)
print(data.head(2))
print(data.tail(2))
print(data.info())
print(data.iloc[1:3])
print(data.loc[1:4])
print(data.drop("category",axis=1))