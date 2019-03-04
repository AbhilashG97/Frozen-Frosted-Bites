# Pandas : Python Data Analysis Library

:warning: The content for this repository is taken from various online resources. 

Please view [this](#) file which contains sample code on the usage of the pandas libaray.

## Basics

### Importing the library 

Before the pandas library can be used, it has to be installed and imported. The pandas documentation provides a detailed explanation on how to install pandas. 

Importing the pandas library is quite simple. It can be done in the following way - 

```python
import pandas as pd
```

:exclamation: Usually, **pandas** is aliased as **pd** for ease of usage.

### Reading from a file

Reading from a file using pandas is really easy. Depending on the type of the file, a suitable method can be selected by suffixing the type of the file in ```read_x```, where ```x``` is a file type. 

Below is table which shows various methods that can be used to read from files of different types - 

| Format Type | Data Description     | Reader         | Writer       |
|-------------|----------------------|----------------|--------------|
| text        | CSV                  | read_csv       | to_csv       |
| text        | JSON                 | read_json      | to_json      |
| text        | HTML                 | read_html      | to_html      |
| text        | Local clipboard      | read_clipboard | to_clipboard |
| binary      | MS Excel             | read_excel     | to_excel     |
| binary      | HDF5 Format          | read_hdf       | to_hdf       |
| binary      | Feather Format       | read_feather   | to_feather   |
| binary      | Parquet Format       | read_parquet   | to_parquet   |
| binary      | Msgpack              | read_msgpack   | to_msgpack   |
| binary      | Stata                | read_stata     | to_stata     |
| binary      | SAS                  | read_sas       |              |
| binary      | Python Pickle Format | read_pickle    | to_pickle    |
| SQL         | SQL                  | read_sql       | to_sql       |
| SQL         | Google Big Query     | read_gbq       | to_gbq       |

Here is an example which shows how to read data from a csv file - 

```python
import pandas as pd

data = pd.read_csv('fileName')
```

:warning: The data that is read form a file is stored in a pandas data structure, such as a [DataFrame](https://pandas.pydata.org/pandas-docs/stable/getting_started/dsintro.html).  

:warning: Depending on the file type, a suitable method can be choosen to read a file.

### Examining the data

```pandas``` also allows the user to examine the data. To exmaine the data the following methods can be used - 

1. ```head()```
1. ```tail()```
1. ```shape```

The above mentioned methods can be used on both ```DataFrame``` and ```Series```. 

Invoking these methods shows a sample of the data, usually upto 5 rows. The ```head()``` function displays the first 5 rows and the ```tail()``` function displays the last 5 rows.

```shape``` returns the size of the data set.

:warning: The pandas Dataframe allows us to store data of differnt types. 

### Indexing data with pandas

One of the ways to index values in pandas is using ```iloc``` and ```loc```. 

1.  **```iloc```**

    In ```iloc``` we specify the data using index values. 

    Here is an exmaple - 

    ```python
    data_portion = data.iloc[1:10, :]
    ```

    The syntax for the command is as follows - 

    ```python
    data.iloc[row, column] 
    ```

1.  **```loc```**

    In ```loc``` the name of the row or the column can be directly specified. There is no need to refer the data through its index.

    Here is an exmaple - 

    ```python
    data.loc[:, "awesome_fruits", "expensive_fruits"]

    data.loc["awesome_fruits", :] 
    ```

There is another method to index the data in pandas, i.e. the data can be accessed directly from the DataFrame by specifying the key of the data as the data is stored in the DataFrame in the form of key-value pairs.

Here is an example - 

```python 
data['row_name']

data['column-name']
```

The above code returns a ```Series```. ```Series``` is one of the data structures present in pandas. A single column of data is stored in a ```Series```.

:warning: A list of columns can also be passed as a key to get the data.  

Here is an example -

```python
data[['column_name_1', 'column_name_2']]
```

### Creating Series and DataFrames

Pandas allows us to create ```Series``` and ```DataFrame``` data structures. 

#### Creation of Series 

A ```Series``` data structure can be created by passing a list as parameter. A ```Series``` data structue holds data stored in columns.

Here is an example - 

```python
series = pd.Series(['watermelon', 'mango', 'apple'])
```

#### Creation of DataFrame

A ````DataFrame``` can be created in a number of ways, some of them are mentioned below -

1.  **Creation from Series**

    A DataFrame can be created from a Series. 

    Here is an example -

    ```python
    my_DataFrame = pd.DataFrame([series_one, series_two])
    print(my_DataFrame)
    ```

1.  **Creation from a dictionary**

    A ```DataFrame``` can also be created from a dictionary. Here, each ```key-value``` pair constitutes a column in a DataFrame. The ```key``` becomes the heading the value is ends up as the data.

    Here is an example - 

    ```python
    my_DataFrame = pd.DataFrame({
        fruits : ['watermelon', 'lychee', 'pineapple', 'mango']
        desserts : ['ice cream', 'popsicle', 'juice', 'shake']
    })
    ```

#### DataFrame methods

This section contains information on the methods used in DataFrames. Most of the methods used in DataFrames are also applicable for Series. 

##### Reading data

Pandas gives the user the ability to access any row(s) or column(s) of a DataFrame. Since, a DataFrame is also like a map, the data can be accessed from it by specifying its key.

Here is an example- 

```python 
data_portion = data['column_name']
```

##### Performing calculations

Pandas also has a few methods which can be used to calculate various statistical parameters. - 

| Pandas DataFrame methods | Method Description                                            |
|--------------------------|---------------------------------------------------------------|
| pandas.DataFrame.corr    | Finds the correlation between columns in a DataFrame          |
| pandas.DataFrame.count   | Counts the number of non-null values in each DataFrame column |
| pandas.DataFrame.max     | Finds the highest value in each column                        |
| pandas.DataFrame.min     | Finds the lowest value in each column                         |
| pandas.DataFrame.median  | Finds the median of each column                               |
| pandas.DataFrame.std     | Finds the standard deviation of each column                   |

:waring: We can either specify the columns on which we want to do the calculations or we can directly use the above mentioned methods, Pandas will find out those columns on which the mathematical operations can be performed and it will do the calculations on those columns only.

Here is an example - 

```python
print(data['some_column'].mean())

print(data.mean())
```

:warning: Also, basic math operations can also be performed on the data.

Here is an example - 

```python 
print(data.mean() / 2)
```

##### Filtering Data Sets 

```Pandas``` can be used to filter the data based on a particular criteria. 

Here is an example - 

```python
filter = data['some_column'] > some_value

new_date = data[filter]
```

:warning: The **````filter```** variable contains a list of boolean values, according to which a new data can be generated. 

:exclamation: Multiple filters can also be applied to a data set by using the ```&```.

Here is an example -

```python 
filter = data[some_column] > value & data[some_column] < value
filtered_data = data[filter]
```
