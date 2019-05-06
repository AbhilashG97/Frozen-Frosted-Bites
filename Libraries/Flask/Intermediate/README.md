# Flask 

This section contains more information on how to use the python flask library to create APIs. 

## API Design Principles

> Two aspects of a good API are usability and maintainability

One of the key points about designing APIs is to format the APIs correctly. 

Here are some points you have to keep in mind - 

1.  Try to build the API in this format - 

    ```https://api.example.com/v1/resources/all```

    :warning: This ensures that the API that you build can be scaled according to its needs.

1.  Documentation is very important when building APIs. No API is complete without proper documentation.
    Tools like [Doxygen](http://www.doxygen.nl/) and [Sphinx](https://www.sphinx-doc.org/en/stable/) can be used for documenting the API. 

    :warning: [Here](http://api.repo.nypl.org/) is sample API documentation. 

## Connecting API to a Database

Please view [this file](https://github.com/AbhilashG97/Frozen-Frosted-Bites/blob/master/Libraries/Flask/Intermediate/Sample%20Code/create_fruitdb.py), which creates a mock database. SQLite3 database has been used here as it has built-in support for it.

After setting-up the database the API can be built. Please view [this file](https://github.com/AbhilashG97/Frozen-Frosted-Bites/blob/master/Libraries/Flask/Intermediate/Sample%20Code/database_api.py) for the sample code.

The sample code has comments which explains what each line of code does. 

:warning: Within a query parameter, spaces between words are denoted with a ```+``` sign, e.g. ```Star+Fruit```.

:sparkles: This completed the intermediate level of flask API creation. :sparkles:

## References

Please have a look at this [blog post](https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask). :heart:
