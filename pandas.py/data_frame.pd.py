import pandas as pd
data={
    "name":["alice","suf","bob","charlie","david"],
    "age":[25,34,24,57,28],
    "department":["HR","IT","FINANCE","MARKETING","SALES"],
    "SALARY":[20000,30000,40000,50000,60000]
}
d=pd.DataFrame(data)
print(d)
print(d.head(3))   #printing the starting elements of the data
print(d.tail(2))  #printing the last elements of the data
print(d.iloc[1:3])
print(d.iloc[[0,2,4]]) 
print(d.loc[1:4,["name","SALARY"]])
print(d.drop("age",axis=1)) #droping the age column
print(d.drop([0,2],axis=0)) #droping the 0 and 2 rows
print(d)
print(d.shape)
print(d.info())
print(d.describe())
d["salary_increase"]=d["SALARY"] + 5000
print(d)
# renaming the columes 
d.rename(columns={"department":"dept"},inplace=True)
print(d)
#to check the unique names
print(d["dept"].unique())
#to check the number of unique names
print(d["dept"].nunique())
#to check the people in each department
print(d["dept"].value_counts())