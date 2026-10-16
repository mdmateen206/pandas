import pandas as pd
s=pd.Series([10,20,30,40,50,"qbc"])
print(s)
print(s.name)
print(s.values)
print(s.index)
s.name="numbers"
print(s)
print(s[0:3])
print(s.iloc[3])
print(s.iloc[[1,3,5]])
index=["a","b","c","d","e","f"]
s.index=index
print(s)
print(s["a"])
print(s.iloc[[2,3,5]])
print(s[0:3])
print(s.loc["b":"d"])
print(s["a":"d"])

