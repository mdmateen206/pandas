import pandas as pd
fruits_cal={
    "apple":0.2,
    "banana":0.3,
    "orange":0.4,
    "grapes":0.5,
    "watermelon":1.3,
    "strawberry":1.4,
    "blueberry":1.7,
    "kiwi":2.0
}
s2=pd.Series(fruits_cal,name="calories")
print(s2)
#using and operator to filter fruits with calories 
print(s2[(s2>0.5) & (s2<1.7)])
#using or operator to filter fruits with calories
print(s2[(s2>0.3) | (s2>2.0)])
#using not operator to filter fruites with calories
print(s2[~(s2<0.4)])

#modifying the calories
s2["banana"]=2.8
print(s2)