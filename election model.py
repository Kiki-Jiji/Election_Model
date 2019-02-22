import os
arr = os.listdir()
arr

import pandas as pd

#Import Raw data
raw_data = pd.read_excel("PollBase-Q4-2018.xls", sheet_name= "10-15")

#slice needed data
full_data = raw_data.iloc[:, 0:17]

#Drop columns of unnessasary data
cols = [3,5,9,11,13,14,15]
data = full_data.drop(full_data.columns[cols], axis=1, inplace = False)

#Rename Columns
data.columns = ['Year', 'Month', 'Fieldwork', 'Published', 'Polling', 'Publisher',
       'Con', 'Lab', 'LD', 'Method_Collection']

"""

Dealing with missing values
There are alot of missing values in the dataframe. For the polling data, it
makes sense to drop any values with NAN in. If other data, such as publisher,
or the methdod of collection are missing then it is far less important if
values are missing.
Recommended approach in data science, create a mask, then use to subset non NAN
values

"""
#Checks whether NAN is always for labour and conservative
x = data["Con"].isnull() == data["Lab"].isnull()
xx = x.sum() / len(x) * 100
print(str(xx) + " percentage of missing values is for both Lab and Con")

#How many missing Values (sum counts all trues )
print("There are " + str(data["Lab"].isnull().sum()) + " missing values")

data1 = data.dropna(subset=["Lab"])

data["Lab"].hist()
