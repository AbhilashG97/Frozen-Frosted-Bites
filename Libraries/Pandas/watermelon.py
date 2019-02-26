# A code snippet to demostrate the use of 
# pandas python library

import matplotlib.pyplot as plt
import pandas as pd

# The data is stored in the pandas DataFrame
reviews = pd.read_csv('data\ign.csv')

# head() prints the initial portion of the data
print(reviews.head())

# tail displays the last portion of the data
print(reviews.tail())

# shape returns the size of the DataFrame
print(reviews.shape)

# Pandas vs just using NumPy is that Pandas allows you 
# to have columns with different data types

# indexing with pandas
# this can be done with iloc and loc

print((reviews.iloc[0:10, :]))

# removing the index column as it is not required anymore

reviews = reviews.iloc[:, 1:]

print(reviews.head())

# indexing using labels in pandas using loc[]

print(reviews.loc[:, 'score'])

# multiple columns can be passed using a list
print(reviews.loc[:, ['score', 'release_year']])

# retrieving columns using Pandas Series Object
print(reviews['score'])

print(reviews[['score', 'release_year']])

# DataFrame stores tabular data, but a Series stores a single column or row of data

# Creating a series object manually

fruit_series = pd.Series(['watermelon', 'lychee', 'strawberry'])
dessert_seies = pd.Series(['watermelon mochi', 'lychee icecream', 'strawberry shortcake'])
print(fruit_series, dessert_seies)
print('\n')

dataframe = pd.DataFrame([fruit_series, dessert_seies])
print(dataframe)
print('\n')

# another way to create a DataFrame in pandas
# column and row names can also be specified using the index and columns argument respectively
my_dataframe = pd.DataFrame([[1, 2, 3], ['watermelon', 'mango', 'lemon']], index=['numbers', 'fruits'], columns=['column1', 'column2', 'column3'])
print(my_dataframe)
print("\n")
# another way to create a DataFrame with column names is to use a dictionary

another_DataFrame = pd.DataFrame({
    'fruits' : ['watermelon', 'apple', 'lychee'],
    'fruit_desserts' : ['watermelon mochi', 'apple pie', 'lychee lemon cake']
})

print(another_DataFrame)

# Pandas DataFrame Methods

# most of the methods are the same in both Series and DataFrame 

print(reviews['score'].tail())

# Series and DataFrames also have other methods that make calculations simpler

print("Mean score of all games is " + str(reviews['score'].mean()))

print(reviews.mean())

# We can also specify the axis while calculating the mean

# axis=0 will calculate the mean of all columns and the axis=1 
# the default value of axis is 0.
print(reviews.mean(axis=1))

# DataFrame Math with Pandas

# Baisc math operations can also be applied to Series or DataFrame objects
print(reviews['score'] / 2)

# Boolean Indexing in Pandas

# We can filter a DataFrame based on a certain criteria 

# Get filter whose score is greater than the average score
score_filter = reviews['score'] > reviews['score'].mean()

# apply the filter to the DataFrame
filtered_reviews = reviews[score_filter]

print(filtered_reviews.head())
print('\n')

filter_platform = reviews['platform'] == 'Xbox One'
XBox_games = reviews[filter_platform]
print(XBox_games.head())
print('\n')

# multiple filters
mixed_filters = (reviews['score'] > reviews['score'].mean()) & (reviews['platform'] == 'Xbox One')
custom_reviews = reviews[mixed_filters]
print(custom_reviews.head())

# Pandas Plotting

custom_reviews['score'].plot(kind='hist')
plt.show()