import pandas as pd
fruit_protin={
    "apple":0.3,
    "banana":0.4,
    "orange":0.5,
    "graps":0.2,
    "avacado":2.0,
    "guava":2.6,
}
s=pd.Series(fruit_protin,name="protein")
print(s)
print(s>1) #return in bollean valuesss
print(s[s>1]) #return key and values pair where condition is  true
print(s.name)
