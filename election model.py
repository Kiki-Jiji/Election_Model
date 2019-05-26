import os
arr = os.listdir()
arr

import pandas as pd
import matplotlib.pyplot as plt


pd.options.display.max_rows=999
pd.options.display.max_columns=999
cols = [3,5,9,11,13,14,15]

#Import Raw data
df = pd.read_excel("PollBase-Q4-2018.xls", sheet_name= "10-15").iloc[:, 0:17]
df= df.drop(df.columns[cols], axis=1, inplace = False ).rename(columns={'Unnamed: 16':'Method'}, index=str)



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
#x = data["Con"].isnull() == data["Lab"].isnull()
#xx = x.sum() / len(x) * 100
#print(str(xx) + " percentage of missing values is for both Lab and Con")

#How many missing Values (sum counts all trues )
#print("There are " + str(data["Lab"].isnull().sum()) + " missing values")

#removes all na values, data left is na free
#data1 is now main dataset
#data1 = data.dropna(subset=["Lab"])

#line plot

#plt.plot(data.loc[:, "Lab"])
#plt.plot(data.loc[:, "Con"])
#plt.legend()


























