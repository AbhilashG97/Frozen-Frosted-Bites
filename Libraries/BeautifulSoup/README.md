# BeautifulSoup Tutorial

This is a short tutorial on BeautifulSoup. Please view [here](https://www.dataquest.io/blog/web-scraping-tutorial-python/) for more details.

## Introduction 

> Beautiful Soup is a Python library for pulling data out of HTML and XML files.

When we want to extract information from a webpage, we are mostly concerned with ```HTML``` as it contains all the content of a webpage.

The webpage has the following contents - 

1.  ```HMTL```
1. ```CSS```
1. ```JS```
1. Image files which end with formats like ```png``` and ```jpeg```.

## Playing around with HTML and CSS

### HTML

This section will explain ```HTML``` briefly. 

:warning: ```HTML``` is a markup language, which tells the browser how to layout content. It is not a programming language. 

In order to scrap data from a webpage we need to know the basic structure of a ```HTML``` document. A ```HTML``` document contains a lot of tags. 

Every ```HTML``` document contains the following tags - 

1.  ```HTML Tag```
    
    All the content of a ```html``` document is inside this tag. Here is an example - 

    ```<html></html>```

1.  ```HEAD Tag```

    This tag contains the heading of a webpage along with other information. 

    :exclamation: This tag isn't that important in data scraping as it doesn't contain much data.

    Here is an example -

    ```<head></head>```

1.  ```BODY Tag```

    This tag contains all the data of the webpage. This is used a lot in data scraping. 

    Here is an example -

    ```<body></body>```

1.  ```P tag```

    This tag is used to add paragraphs inside the body of a html page.

The tags can also be classified into the following types - 

1.  **```parent```**

    The parent tag contains other contains other tags. For e.g, the ```html tag``` is the parent of the ```body tag```.

1.  **```child```**

    A child tag is nested inside another tag. For e.g, the ```<p>``` tag is a child of the ```<body>``` tag.

1.  **```sibling```**

    A sibling tag is one which is nested inside the same parent tag. 

### CSS 

This section will explain the ```ids``` and ```classes``` that are used in ```CSS```.

:warning: One element can have multiple classes, and a class can also be shared between elements.

:warning: Each element can only have one id, and an id can only be used once on a page.

:exclamation: Classes and ids are optional and not all elements will have them.

## The requests library


[This file](https://github.com/AbhilashG97/Frozen-Frosted-Bites/blob/master/Libraries/BeautifulSoup/watermelon.py) contains sample code.

### Downloading a webpage 

Before we can start scraping data from a webpage, we'll have to download it. Therefore, the first thing that needs to be done is to download the webpage to be scrapped. 

In order to download a webpage we make use of the requests library's ```get()``` function. The example for the same is given below -

```python 
import requests 

page = requests.get('https://www.somewebpage.com')
print(page.status_code)
```

If the webpage has been downloaded correctly we should see a stutus code that starts with ```2```. 

:warning: In order to view the status code of a webpage the ```status_code``` property has to be invoked. 

:warning: If we get a status code that starts with 4 or 5, then some error has occurred. 

:warning: The ```html``` of the downloaded webpage can be viewed by making use of the ```content``` attribute. 

### Parsing a webpage with BeautifulSoup

This section will contain information on how to parse a ```html document```. 

We first have to import the ```BeautifulSoup module```. 

Here is an example - 

```python 
from bs4 import BeautifulSoup

watermelon = BeautifulSoup(watermelon_page.content, 'html.parser')
print(watermelon.prettify())
```
:warning: After importing the BeautifulSoup module, an instance of the BeautifulSoup has to be created.

:warning: The ```prettify()``` method is used to make the html content look pretty and easy to read.

