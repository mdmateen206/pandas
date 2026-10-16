import pandas as pd
data={
    "name": ["john", "marry", "peter", "jane", "doe"],
    "age":[23,24,25,None,27],
    "dep":["it","hr","finance","hr",None],
    "salary":[5000,4000,None,4500,None]
}
d=pd.DataFrame(data)
print(d)
data1={
    "name": ["kishor", "sadiq", "jupiter", "jain", "dog"],
    "age":[23,24,25,None,27],
    "dep":["it","hr","finance","hr",None],
    "salary":[5000,4000,None,4500,None]
}
d1=pd.DataFrame(data1)
print(d1)
print(pd.concat([d,d1],axis=0))
print(pd.concat([d,d1]))
print(pd.merge(d,d1,on="dep"))
print(pd.pivot_table(d1,index="dep",values="salary"))
