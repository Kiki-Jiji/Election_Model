import os
arr = os.listdir()

import pandas as pd
import numpy as np

pd.options.display.max_rows=999
pd.options.display.max_columns=999


#Import data
df = pd.read_excel("PollBase-Q4-2018.xls", sheet_name= "10-15").iloc[:, 0:17]
df= df.drop(df.columns[[0,1,2,4,5,9,11,13,14,15]], axis=1, inplace = False ).rename(columns={'Unnamed: 16':'Method', 'Unnamed: 3': 'Date'}, index=str)

#Finds missing polling data. As lab, con and lib all have the same missing data then used lab column. Could only do by numpy 
missing = np.asarray(df.loc[pd.isna(df["Lab"])].index)

#Remove rows
df= df.drop(index=missing)

