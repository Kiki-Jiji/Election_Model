import os
arr = os.listdir()
arr

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pd.__version__

#Import Raw data
raw_data = pd.read_excel("PollBase-Q4-2018.xls", sheet_name= "10-15", 
                         skipfooter= 4)

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

#removes all na values, data left is na free
#data1 is now main dataset
data1 = data.dropna(subset=["Lab"])

#line plot

plt.plot(data.loc[:, "Lab"])
plt.plot(data.loc[:, "Con"])
plt.legend()

# Fix date
#First year- need to copy year cell downwards 
data1["Year"] = data1["Year"].replace(0, np.nan).ffill().astype(int)

#there are missing values for published, whoch is the day, need to fill in as 
#don;t want to lose data. current method, forward propagate values (nan become 
#the previous value)
data1["Published"] = data1["Published"].fillna(method = "ffill")


#combines the columns together
cols = ["Published", "Month", "Year",]
data1["Date"] = data1[cols].apply(lambda row: " ".join(row.values.astype(str)), axis=1)


""" The following works, ish,
it does convert the date column to a datetime object, but throws up a warning

use option to turn off SettingWithCopyWarning , bad idea! but don;t know
why the error is generated 


probably best not to use following line but option to deal with errors
# pd.options.mode.chained_assignment = None
"""

# Should convert to datetime object, does not!
data1["Date"] = pd.to_datetime(data1["Date"], errors = "coerce")

#Droping unnessary columns 
col1 = [0,1,2,3]
data1.drop(data1.columns[col1], axis=1, inplace=True)














