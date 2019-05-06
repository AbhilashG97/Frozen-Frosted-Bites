# Flask Basics

## What is an API?

>  The term API, short for Application Programming Interface, refers to a part of a computer program designed to be used or manipulated by another program, as opposed to an interface designed to be used or manipulated by a human. 

:warning: Here APIs will refer to Web APIs. 

:boom: At times it may be feasible to provide a ```data dump``` in the form of a downloadable JSON, XML, CSV, or SQLite file. In certain cases both an API and a data dump can be provided. 

## Common Web API Terminology

1.  **HTTP** :
    ```Hypertext Transfer Protocol``` is the primary means of communicating data on the web. HTTP implements a number of ```methods```, which tell which direction data is moving and what should happen to it. 

1.  **URL**
    ```Uniform Resource Locator```is an address for a resource on the web. It consists of a ```protocol```, ```domain``` and ```path```(optional).

1.  **JSON**
    ```JavaScript Object Notation``` is a text-based data storage format.

1.  **REST**
    ```REpresentational State Transfer``` is a philosophy that describes some best practices for implementing APIs.

## Other Frameworks for creating API

```Flask``` is not the only Framework that can be used to create APIs, there are other frameworks such ```Django REST Framework```, ```Tastypie``` and others.

Here we'll be using at ```Flask``` to create APIs.

## Creating a simple Flask application

Setup the proper directories for the flask application. 

:exclamation: Please refer to the ```Sample Code``` directory for sample programs written using the Flask Framework. 

:warning: The ```hello_world.py``` file contains a very simple flask web application that runs in the web browser. You can have a look at the file [here](https://github.com/AbhilashG97/Frozen-Frosted-Bites/blob/master/Libraries/Flask/Basics/Sample%20Code/hello_world.py).

## Explanation for the sample app

Please have a look at this [file](https://github.com/AbhilashG97/Frozen-Frosted-Bites/blob/master/Libraries/Flask/Basics/Sample%20Code/hello_world.py)

The first line is an ```import statement``` which imports the flask library. 

The third line creates the flask object with which we can invoke various methods such as the ```app.run()``` method.

The fourth line is starts the debugger. 

The sixth and the seventh line links a HTTP method to a python function. 

And the last line starts the web application. 

## Creating the API

The API data is created as a ```list of Python dictionaries```.

Here is an example - 

```python
[
    {
        'name': 'Watermelon',
        'price': '55'
    },
    {
        'name': 'Banana',
        'price': '25'
    }
]
```

A sample python code can be found in the ```sample code``` directory. Please view this [file](https://github.com/AbhilashG97/Frozen-Frosted-Bites/blob/master/Libraries/Flask/Basics/Sample%20Code/json_data.py).

In the above mentioned sample code, we have created a simple json data which can be accessed through ```routing```. ALso, the ```jsonify()``` function was used which coverts a list of dictionaries to a json data. 

:exclamation: The process of mapping URLs to functions is called **routing**.

## Resource Specific API

We can also construct APIs that are resource specific. Please view [this file](https://github.com/AbhilashG97/Frozen-Frosted-Bites/blob/master/Libraries/Flask/Basics/Sample%20Code/filtered_api.py) for the sample code.

The query can be added to the url like this - ```?id=0```

In order to get the query parameter from the url, ```request.args``` is used. If the query parameter is present, the parameter is selected and the corresponding item from the dictionary is selected and returned. 

<hr>

:sparkles: Yay! This finishes the basics of the flask library for creating APIs. :sparkles:
