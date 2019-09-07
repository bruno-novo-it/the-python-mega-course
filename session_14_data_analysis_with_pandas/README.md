
###### Install Pandas
```
pip3 install pandas
```
###### Install iPython
```
pip3 install ipython 
```

import pandas
df1=pandas.DataFrame([[2,3,4],[10,20,30]])

df1 = pandas.DataFrame([[2,3,4],[10,20,30]],columns=["Price","Age","Value"])

df1 = pandas.DataFrame([[2,3,4],[10,20,30]],columns=["Price","Age","Value"],index=["First","Second"])

type(df1)

df2 = pandas.DataFrame([{"Name":"John"},{"Name":"Jack"}])


### A DataFrame is made of Series

type(df1.mean()) --> pandas.core.series.Series

type(df1.Price) --> pandas.core.series.Series