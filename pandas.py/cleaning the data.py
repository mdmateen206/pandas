import pandas as pd
data={
    "name":["alice","suf","bob",None,"david"],
    "age":[25,34,24,None,28],
    "department":["HR","IT","FINANCE","HR","IT"],
    "SALARY":[20000,30000,40000,None,60000]
}
d=pd.DataFrame(data)
print(d)
#to check the null values in the data
print(d.isnull().sum())
#to drop the null values
print(d.dropna())
#filling the null values with a specific value
print(d.fillna(0))
#filling the null values with the mean 
print(d.fillna(d.mean(numeric_only=True)))
#filling the particular column with the mean
print(d["SALARY"].fillna(d["SALARY"].mean()))
#filling the particular column with the median
print(d["age"].fillna(d["age"].median()))
#replacing the values
print(d["name"].replace("suf","ayush"))
#duplicates
print(d.duplicated())