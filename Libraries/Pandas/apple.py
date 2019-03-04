# A code snippet to demostrate the use of 
# pandas python library 

import pandas as pd

data = pd.read_csv('data/food.csv')
print(data.head())
print(data.shape)

data = data.loc[:, 'RespondentID':]
print(data.head())
print(data.shape)

data_filter = data.