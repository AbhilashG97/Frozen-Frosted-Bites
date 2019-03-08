# A code snippet to demostrate the use of 
# pandas python library

import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt

# reading data from a file

data = pd.read_csv('data/food.csv')
print(data.head())
print('The size of the data set is' + str(data.shape))
print()

# Getting the names of all the columns

column_names = data.columns[:]
print('The name of all the columns are - ')
print(column_names)
print()

# Finding unique values in a column 
values = data['Do you celebrate Thanksgiving?'].unique
print(values)
print()

# Getting the count of all the values in a column
print(data['What is your gender?'].value_counts(dropna=False))
print()

# a function to change the value of the gender field
def gender_code(gender_string):
    if isinstance(gender_string, float) and math.isnan(gender_string):
        return gender_string
    return int(gender_string == 'Female')

# Transforming the values of a column in the data set
# The apply method transforms the Series 
data['gender'] = data["What is your gender?"].apply(gender_code)
print(data['gender'].value_counts(dropna=False))
print()

# applying a function to a column using a lambda expression
print(data.apply(lambda x: x.dtype).tail(25))
print()

# analyzing a column
print(data['How much total combined money did all members of your HOUSEHOLD earn last year?'].unique)
print(data['How much total combined money did all members of your HOUSEHOLD earn last year?'].value_counts(dropna=False))
print()

# a function to transform data in a column
def clean_income(value):
    if value == 'Prefer not to answer':
        return np.nan
    elif value == '$200,000 and up':
        return np.nan
    elif isinstance(value, float) and math.isnan(value):
        return value
    else:
        value = value.replace(',', '').replace('$', '')
        low_value, high_value = value.split(' to ')
        return (int(low_value) + int(high_value)) / 2

# transform a column in the data set
data['income'] = data['How much total combined money did all members of your HOUSEHOLD earn last year?'].apply(clean_income)
print(data['income'].value_counts(dropna=False))
print()

# analyzing the data 
print(data['What type of cranberry saucedo you typically have?'].value_counts(dropna=False))
print()

# GROUPING A DATA SET  

# creating a data set based in a filter 
canned = data[data['What type of cranberry saucedo you typically have?'] == 'Canned']
homemade = data[data['What type of cranberry saucedo you typically have?'] == 'Homemade']

print(canned.head(20))
print()

print(homemade.head(20))
print()

canned_income = canned['income'].mean()
homemade_income = homemade['income'].mean()

print(f'The income for those who eat canned and homemade cranberry sauce is as follows {canned_income, homemade_income}')
print()

# the above method of grouping data by providing a filter is not efficient,
# there is another way to group data in python by making use of the groupby method
grouped_data = data.groupby('What type of cranberry saucedo you typically have?')
# the groupby method returns a DataFrameGroupBy Object
print(grouped_data.head())
print()

# displays all the groups in the geouped data frame 
print(grouped_data.groups)
print()

# the size method returns the number of rows in each group present in data group
print(grouped_data.size())
print()

# a simple for loop can be used to iterate through the data present in the DataFrameGroupObject
for name, group in grouped_data:
    print(name)
    print(group['What type of cranberry saucedo you typically have?'])
    print(type(group))

# NOTE: DataFrameGroupBy object contains multiple DataFrames

# Extracting a column from a DataFrameGroupBy Object
print(grouped_data['income'].size())
print()

# AGGREGATING VALUES IN GROUPS
# The data present in the DataFrameGoup Object can be aggregated
print(grouped_data['income'].agg(np.mean))

# NOTE: If nothing is specified, mean will be calculated for all those columns on which arithmetic calculations 
# can be performed

# PLOTTING GRAPHS 
grouped_data['income'].plot(kind='bar')
plt.show()

# many columns in the data set can be grouped together too
another_grouped_data = data.groupby(['What type of cranberry saucedo you typically have?', 'What is typically the main dish at your Thanksgiving dinner?'])
print(another_grouped_data.groups) 

# The grouped data can be aggregated in multiple ways 
print(another_grouped_data.agg([np.mean, np.sum, np.std]).head(25))

watermelon_data = data.groupby('How would you describe where you live?')['What is typically the main dish at your Thanksgiving dinner?']
watermelon_data.apply(lambda x:x.value_counts())