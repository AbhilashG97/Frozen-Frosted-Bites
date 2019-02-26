# Pandas : Python Data Analysis Library

:warning: The content for this repository is taken from various online resources. 

Please view [this](#) file which contains sample code on the usage of the pandas libaray.

## Basics

### Importing the library 

Before the pandas library can be used, it has to be installed and imported. The pandas documentation provides a detailed explanation on how to install pandas. 

Importing the pandas library is also quite simple. It can be done in the following way - 

```python
import pandas as pd
```

:exclamation: Usually pandas is aliased as pd for ease of usage.

### Reading from a file

Reading from a file using pandas is really easy. Depending on the type of the file, a suitable method can be selected by suffixing the type of the file. 

Below is table which shows the variuos methods that can be used to read from various files - 

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

Here is an exmaple which shows how to read data from a csv file - 

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

1.  **```loc[]```**

    In ```loc``` the name of the row or the column can be directly specified. There is no need to refer the data through its index.

    Here is an exmaple - 

    ```python
    data.loc["awesome_fruits", "expensive_fruits"]

    data.loc["awesome_fruits", :] 
    ```

There is another method to index the data in pandas, i.e. the data can be accessed directly from the DataFrame by specifying the key of the data as the data is stored in the DataFrame in the form of key-value pairs.

Here is an example - 

```python 
data['row_name']

data['column-name']
```

