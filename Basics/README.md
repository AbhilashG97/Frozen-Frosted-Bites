# Python Basics :snake:

## Introduction 

Python code is translated into intermediate code, which has to be executed by a virtual machine, known as the **PVM**, the **Python virtual machine**. This is a similar approach to the one taken by Java. There is even a way of translating Python programs into Java byte code for the Java Virtual Machine (JVM). This can be achieved with **Jython**.

To compile a python program we use the ```py_compile``` module. 

The syntax looks something like this - 

```python
python -m py_compile my_first_simple_script.py
```

We can also use ```compileall``` to compile all the python programs in a given directory.

The syntax for this looks something like this - 

```python 
python -m compileall .
```

:warning:   First, there will be a new subdirectory **__pycache__**, if it hasn't already existed. You will find a file ```my_program.pyc``` in this subdirectory. This is the compiled version of the file in byte code.

:warning:    If Python has write-access for the directory where the Python program resides, it will store the compiled byte code in a file that ends with a ```.pyc``` suffix. If Python has no write access, the program will work anyway. The byte code will be produced but discarded when the program exits.

:warning:   Whenever a Python program is called, Python will check, if there exists a compiled version with the .pyc suffix. This file has to be newer than the file with the .py suffix. If such a file exists, Python will load the byte code, which will speed up the start up time of the script. If there exists no byte code version, Python will create the byte code before it starts the execution of the program. 

:exclamation: Execution of a Python program means execution of the byte code on the Python Virtual Machine (PVM).

:warning: Python does not do implicit casting, as implicit casting can mask critical logic errors. Therefore, if we want to concatenate any object with a string in python we can to either explicitly use the ```str``` function or we have to use any string formatter in Python. 


## Programming in Python 

This document will contain a short demo of the python language - 

### Loops

Loops in python follow this syntax -

```python
for token in tokens:
```
:warning: To print items of a collection in single line, you have to do the following:

```python
for(item in items)
    print(item, end=" ")
```

### Strings

Strings are immutable in python. They can be enclosed in single, double, triple quotes.

Example - 

1. ```"text"``` OR ```""text""``` OR ```"""text"""```
1. ```'text'``` OR ```''text''``` OR ```'''text'''```
    
:warning: Strings in triple quotes can be written in multiple lines.

:warning: Multiplication can also be performed on strings.

```python 
    print(".-." * 4)
```

:warning: A string in Python consists of a series or sequence of characters. 

We can also use indices to access characters of a String. We can refer to the characters of a string in the usual way as -  

```python
fruit = "watermelon"

print(fruit[0])
```

:warning: Python also allows us to access characters from a string from the last index too. We can do that with the help of the following example. 

```python

fruit = "watermelon"

print(fruit[-1])
```

:warning: Strings are immutable in Python.

#### Some operations on String 

Here are some operations that can be performed with Strings in Python - 

1.  **Concatenation:**
    
    We can concatenate Strings in Python using the ```+``` operator. 

    ```python
    print("watermelon"+" is delicous")
    ```

1.  **Repetition:**
    
    We can also repeat a string **n** times. 

    ```python
    print("watermelon" * 10) 
    ```

1.  **Indexing:**

    We can index a particular character of string. The format for the same is given above.

1.  **Slicing:**

    We can also slice strings. Slicing can be done by following the given syntax- 

    ```python 
    print("watermelon "[2:4])
    ```

    :warning: In the syntax ```[a:b]```, a is **inclusive** and b is **exclusive**.

1.  **Size**

    We can find the size of a string in Python using the len() function. 

    Example - 

    ```python
    fruit = "watermelon"
    len(fruit)
    ```

#### String Pecularities

Strings show a peculiarity when the ```is``` operator is used. The ```is``` operator checks if two strings share the same idetity. 
If the ```is``` operator returns true for two strings it implies that the two strings are equal. 

i.e. if ```a is b``` returns true, then ```a == b```. However, the converse is not true. If ```a == b``` returns true, then ```a``` may or may not have the same identity ```b```.

#### Escape Characters 

There are a few escape character in Python and they can be used to escape various characters.

Some of the most common used escape characters are mentioned below - 

| Escape Sequence |        Meaning Notes       |
|-----------------|:--------------------------:|
| \newline        |           Ignored          |
| \\              |        Backslash (\)       |
| \'              |      Single quote (')      |
| \"              |      Double quote (")      |
| \v              |   ASCII Vertical Tab (VT)  |
| \t              | ASCII Horizontal Tab (TAB) |

### Indentation 

A block is a group of statements in a program or script. Usually it consists of at least one statement and of declarations for the block, depending on the programming or scripting language. A language, which allows grouping with blocks, is called a **block structured language**.

```Python``` programs get structured through indentation, i.e. code blocks are defined by their indentation. All statements with the same distance to the right belong to the same block of code, i.e. the statements within a block line up vertically.

### Variables and Data Types 

**id Function**

The ```id()``` function can be used to uniquely identify variables in python. Every variable, object has a unique id associated with it.

:warning: Data in a Python program is represented by objects. The objects can be - 

1. built-in, i.e. objects provided by Python   
1. objects from extension libraries  
1. created in the application by the programmer.

**Literals**

Python's build-in core data-type is also called object type.

There are four built-in types for numbers - 

1. Normal Integers
1. Octal Literals (0o21)
1. Hexadecimal Literal (0x1A)
1. Binary Literal (0b001010)

:warning: bin(), hex(), and oct() functions can be used to create binary numbers for a given integer.

:warning: Integers in Python3 can be of **unlimited size**.

:exclamation: There is no "long int" in Python3 anymore. There is only one "int" type, which contains both "int" and "long" from Python2

**Complex Numbers**

Complex numbers are written as ```<real part> + <imaginary part>j```

The syntax for this is something like this - 

```python
x = 2 + 3j
y = 3 + 4j
```

**Integer Division**

There are **two** kinds of division operators:

1. "true division" performed by ```/```
2. "floor division" performed by ```//```

:warning: ```//``` is faster than int(a/b);

### Python Operators

Python provides us many operators to work with. Below mentioned are some of the operators which I found different from the rest of the programming languages.

1.  **Exponentiation**

    The exponentiation operator is given by ```**```. Here is an example for it - 
    
    ```python
    a = 9
    print(a ** 10)
    ```

    :warning: To convert a integer to a string str can be used. 

1. **Element of operator**

    This operator is used to check if an element belongs to a given collection or not.

    Here is an example -

    ```python
    a in [a, b, c]
    ```

    :warning: It can also be used as an iterrator.

    ```python
    fruits = ['watermelon', 'apple', 'mango', 'banana', 'lemon']

    for fruit in fruits:
        print(fruit)
    ```

### Sequential Data Types  
 
Sequences are one of the principal built-in data types besides numerics, mappings, files, instances and exceptions. Python provides for six sequence (or sequential) data types:

1. strings
1. byte sequences
1. byte arrays
1. lists
1. tuples
1. range objects

The above mentioned sequential data types may look different but nevertheless they the following underlying concepts in common- 

1. The items or elements of strings, lists and tuples are ordered in a defined sequence
1. The elements can be accessed via indices

:warning:   Python uses the same syntax and function names to work on sequential data types. This means that we can do the following -

```python
fruits = ["watermelon", "apple", "dragon-fruit", "lemon"]

favorite_numbers = [2, 202, 12092, 23]

print(len(fruits), len(favorite_numbers)) 
```

#### Python Lists

Generally speaking a **list** is an collection of objects. To be more precise: ```A list in Python is an ordered group of items or elements.```

:warning: It's important to notice that these list elements don't have to be of the same type.

A few properties of Python lists are mentioned below -

1. They are ordered
1. The contain arbitrary objects
1. Elements of a list can be accessed by an index
1. They are arbitrarily nestable, i.e. they can contain other lists as sublists
1. Variable size
1. They are mutable, i.e. the elements of a list can be changed

**Syntax**

List objects are enclosed by square brackets and separated by commas. Here are some examples - 

```python
fruits = ["watermelon", "banana", "lyhcee", "black-sapote"]
stuff = ["watermelon", 20, 'A', "Ice-cream"] 
```

**Accessing List elements**

We can access list elements through its index. Here is an exmaple - 

```python
fruits = ["lychee", "watermelon", "pine-apple", "lemon", "mango"]

print(fruits[1], fruits[-1])

```

**Sublists**

A Python list can have nested lists inside of a list. Here is an exmaple - 

```python
fruit_desserts = [["watermelon", ["watermelon-ice-cream", "watermelon-cupcake", "watermelon-pie"]], ["mango", ["mango-ice-cream", "mango-cupcake", "mango-pie", "mango-pizza"]]]

print(fruit_desserts)
```

**Tuples**

A **tuple** is an **immutable list**, i.e. a tuple cannot be changed in any way once it has been created. A tuple is defined analogously to lists, except that the set of elements is enclosed in parentheses instead of square brackets. 

The rules for indices are the same as for lists. 

:warning: Once a tuple has been created, you can't add elements to a tuple or remove elements from a tuple.

Why use Tuples?

Here are some reasons as to why you might consider using tuples - 

1. Tuples are faster than lists.
1. If you know that some data doesn't have to be changed, you should use tuples instead of lists, because this protects your data against accidental changes.
1. The main advantage of tuples consists in the fact that tuples can be used as keys in dictionaries, while lists can't.

Below is a code snippet which shows how to use a tuple - 

```python 
my_favorite_fruits = ("watermelon", "watermelon", "watermelon", "watermelon")

print(my_favorite_fruits[len(my_favorite_fruits)-1])
```

**Slicing**

Slicing can be used to extract an element from a list. The syntax for the slice operator is given below - 

```python
[a:b]  
```

where ```a``` is the start-index (**inclusive**) and b is the end-index (**exclusive**).

Here is an example for the same - 

```python
fruits = ["mango", "pine-apple", "apple", "lemon", "lychee"]
print(fruits[0:3])
```

Even this is correct - 

```python
print(fruits[:3])
```

:warning: We can also have a list which does not contain a few elements. The snippet shown below will print elements that do not have the last two items from the list. 

```python
print(fruits[:-2])
```

:warning: We can also provide a third operator to the slice operator. The third argument is the ```step```. The syntax for using the third operator is given below - 

```python
[a:b:c]
```

```a``` is the start index (**inclusive**), b is the end index (**exclusive**) and ```c``` is the step, which represents how much  to step over each element.

Here is an example for on the it - 

```python
watermelon = "Watermelon is an awesome fruit!"

print(watermelon[::2])
```

**Length**

```len()``` can be used to calculate the length of a string, tuple, list.

**Concatenation of sequences**

Concatenation of sequences like string, lists, tuples etc is quite simple in Python. 

The ```+``` operator can be used to concatenate sequences.

Here are examples for the same - 

```python 

awesome_fruits = ["watermelon", "mango", "lychee", "kiwi", "dragon-fruit"]
okayish_fruits = ["apple", "banana", "orange", "sapote"]

fruits = awesome_fruits + okayish_fruits
print(fruits)

a = "Watermelon"
b = "heart"

watermelon = a + b

print(watermelon)
```

:warning: The augmented assignment ```+=``` which is well known for arithmetic assignments work for sequences as well.

### More on Python Lists

```Python``` list is more like a **stack** and it stores elements in ```First-In-Last-Out``` order. ```Python``` provides us the following methods to work on lists - 

1.  ```append()```
    This method adds an element to the list. The element is added in ```First-In-Last-Out``` order. 

    Here is an example - 

    ```python 
    awesome_list.append("watermelon")
    ```

1.  ```pop()```
    pop() removes the top most element from the list and also returns it. 

    Here is an example - 

    ```python
    fruit = awesome_list.pop()
    ```

1.  ```peak()```

    ```peek()``` function is not available in ```Python```. We have to use a work around for it. We make use of the slicing operator to get the top most element from the list. 

    Here is an example for the same - 

    ```python
    element = list[-1]
    ```
### Extending a list

If we want to add a list to a predefined list at the end, we can make use of the extend keyword. 

:warning: The ```append``` keyword can also be used, but that will result in a sub-list being added to the list. Instead, we have to use the ```extend``` keyword to add items present in the other list. 

Here is the code snippet that shows the same - 

```python
awesome_fruits = ['watermelon', 'guava', 'kiwi', 'mango', 'lychee']
good_fruits = ['dragon-fruit', 'sapote', 'tamarind']

awesome_fruits.append(good_fruits)
good_fruits.extend(awesome_fruits)

print(weird_fruit_salad)
print(awesome_fruit_salad)
```

:warning: We can also use the ```+``` operator to append lists. Below is an example that shows the same - 

```python
list_a = ["orange", "mango", "lemon"]
list_b = ["potato", "chilli", "pepper"]

print(list_a + list_b)
```

:warning: However, please don't use the ```+``` operator in the below mentioned way. 

```python
list_a = list_a + list_b
```

The above code produces the same result but it is computationally very expensive. Instead, we should use the ```append``` or ```extend``` depending on our needs.

:exclamation: It is however better to use ```append``` to append items to a pre-defined list as the append method is comparatively faster than using the ```+``` operator.

### Removing an element from a list

To remove an element from a list we can use the remove method. Here is an example for the same - 

```python

some_list = ["apple", "mango", "pine-apple", "lemon"]
print(some_list)

print("After removing an item .....")
some_list.remove("apple")

```

:warning: We have to specify the value present inside the list rather than it's index in the remove method.

### Finding the position of an element in the list

We can find the position of an element in the list by making use of the ```index()``` method.

Here is an example - 

```python
some_list["element 1"]
```

:warning: The index method also takes in few other parameters as well. The index method takes in three parameters which are - 

1. The element present in the list.
1. The start index.
1. The end index.

Here is an example for the same - 

```python
colors = ["red", "blue", "green", "pink", "orange", "blue", "green"]
print(colors.index("green", 3, len(colors)))
```

### Inserting elements from the list

We can insert elements into a list by using the ```insert()``` command. The syntax for the command is as follows - 

```python
insert(index, element_to_be_inserted)
```

:warning: The insert function places the element to be inserted before the specified index.

```python
some_boring_list = ["Apple", "Orange", "Coffee", "Melon", "Grapes"]
some_boring_list.insert(1, "watermelon")
some_boring_list
```

### Shallow and Deep Copying in Python

When two lists refer to the same value present in the same memory location, and when a change is made to that value, then the values of both the lists change.

Here is an example depicting that scenario - 

```python
list_a = ["watermelon", "lychee", "apple", "mango", "tamarind"]
list_b = list_a

print(id(list_a), id(list_b))
print(list_a, list_b)

list_b[3] = "lemon"

print(list_a, list_b)
print(id(list_a), id(list_b))
```

:warning: In order to prevent this from happening we can make use of **shallow copy** feature of ```Python```. This can be done by making use of the **slicing operator**.

Here is an example for the same - 

```python
some_list = list_a[:]
```

If we make use of this operator, the list is copied using **shallow copy**. In shallow copy, two lists having the same value don't get affected in any way, if the values of any of the lists are changed. 

:warning: We can make use of **Deep copy** to copy elements from one list to another. In **deep copy** if any change is made to one list the other list gets automatically updated. 

Here is an example on the usage of **deep-copy** - 

```python
from copy import deepcopy

sweet_list = ["sugar", "jalebi", "icecream"]
sweet_copy = deepcopy(sweet_list)

print(sweet_list, sweet_copy)
```

### Dictionaries

This section will be about dictionaries in ```Python```. Dictionaries are like lists can be **shrunk** or **grown** by the user as when she/he pleases. They shrink and grow without the need of making copies. 

:exclamation:**NOTE:** Dictionaries can be contained in lists and vice versa.

#### Dictionaries vs Lists

A list is an ordered sequence of objects whereas a dictionary is an unordered set. However, the main difference between a list and a dictionary is that in dictionary the items are accessed via their keys and not their indices.

:warning: Every key in ```Python``` has a value associated with it. The values in the dictionaries can be any ```Python``` data type.  

:warning: Dictionaries are unordered key-value pairs. They are also implemented as hash tables. 

Here is a simple example on how to create a dictionary - 

```python
awesome_fruit_desserts = {
    "watermelon" : "watermelon mochi",
    "banana" : "banana sundae",
    "strawbeery" : "strawberry shortcake"
}
```
For more examples on dictionaries and their usage, please check out [this](https://github.com/AbhilashG97/Frozen-Frosted-Bites/blob/master/Basics/lychee.py) fruity file.

:warning: As dictionaries are unordered, the items stored in dicitionaries are stored in any specific order.

:warning: Also, only immutable objects can be stored as keys in dictionaries. If an mutable object is used as a key in a dictionary, ```Python``` will raise an error. This means that lists and dictionaries cannot be used as keys in Python. However, tuples can be used as keys in dictionaries as they are immutable.

Here is an example  - 

```python
god_level_fruits = ("watermelon", "lychee", "apple", "mango", "grapes")
hellish_fruits = ("banana", "dragon fruit", "sapote")

fruity_stuff = {
    god_level_fruits : "fruity awesomeness",
    hellish_fruits : "why don't you taste good?!"
}
```

#### Operators on Dictionaries

Some operators used on dictionaries are given below :

| Operator         | Explanation                                                                 |
|------------------|-----------------------------------------------------------------------------|
| ```len(d)```     | returns the number of stored entries, i.e. the number of (key,value) pairs. |
| ```del d[k]```   | deletes the key k together with his value                                   |
| ```k in d```     | True, if a key k exists in the dictionary d                                 |
| ```k not in d``` | True, if a key k doesn't exist in the dictionary d                          |

#### pop() and popitem()

```pop()``` and ```popitem()``` can be used to remove an item from a dictionary. The ```pop()``` command removes a key and also returns the value associated with the removed key. 

:warning: If however the key specified in the ```pop()``` command is not present in the dictionary then a key error will be raised. 

:exclamation: To avoid getting errors we can also provide an optional argument in the ```pop()``` function. The optional argument is considered when the specified key is not present in the dictionary. 

:warning: The ```popitem()``` method removes an entry randomnly from the dictionary. This method returns a tuple of size 2, which contains both the removed key and value pair from the dictionary.

Here is an example  - 

```python
fruit_dessert = {
    "watermelon" : "watermelon mochi",
    "banana" : "banana ice-cream sundae",
    "lychee" : "lychee ice cream",
    "lemon" : "lemonade"
}

removed_item = fruit_dessert.pop('lemon')
another_removed_item = fruit_dessert.pop('dragon fruit', 'cherry')


removed_items = fruit_dessert.popitem()
```

#### Accessing non Existing Keys

Acessing elements in the dictionary that do not exist result in errors. In order to avoid that we can make use of the ```in``` keyword. The ```in``` keyword checks whether the key exists or not and returns a boolean value corresponding to the result.

Here is an example - 

```python
fruit_dessert = {
    'mango' : 'mango shake',
    'cherry' : 'dry cherry pops'
}

print(mango in fruit_dessert)
```

#### Some other important methods

1.  **```copy()```**

    A dictionary can copied with the copy method.

    Here is an example for the same - 
    
    ```python
    fruits = {
        "tasty" : "watermelon",
        "not tasty" : "banana"
        "very very tasty" : "yellow watermelon"
    }

    duplicate_fruits = fruits.copy()
    ```
    :warning: The ```copy()``` method performs a shallow copy and not deep copy.

1.  **```update()```**

    We can also merge dictionaries by making use of the ```update()``` method.

    Here is an example - 

    ```python

    fruits = {
        "tasty" : "watermelon",
        "not tasty" : "banana"
        "very very tasty" : "yellow watermelon"
    }

    desserts = {
        "tasty" : "watermelon mochi"
        "not tasty" : "banana mochi"
    }

    desserts.update(fruits)
    ```

#### Iterating over a Dictionary

We can also iterate over the keys of a dictionary. 

Here is an example - 

```python
for fruit in fruits: 
    print(fruit)
```

or ```keys()``` method can also be used.

```python
for fruit_key in fruit.keys():
    print(fruit_key)
```

To iterate over the values of a dictionary we use the ```values()``` method.

Here is an example for the same - 

```python
for fruit_value in fruit.values():
    print(fruit_value)
```

or we can also access the values of the corresponding keys in the dictionary.

```python
for key in fruits: 
    print(fruits[key])
```

:warning: The above method of iterating a dictionary is not good.  The above-mentioned method is quite slow as compared to one described initially.

#### Lists and Dictionaries

Python allows to convert a list to a dictionary and a dictionary to a list.

1.  **List to Dictionary conversion**

    A list can be converted to a dictionary in the following way - 

    1. Use the ```zip()``` function to get a list iterator.
    1. Pass the list iterator to the ```dict()``` function which will generate a list from the dictionary.

Here is an example for it -

```python
    dessert = ["watermelon mochi", "lime tart", "banana ice-cream sundae", "lychee icecream"]
    fruit = ["watermelon", "lemon", "banana", "lychee"] 

    dessert_fruit_dictionary = dict(zip(dessert, fruit))
```

There is another way to do the same thing, however it is recommended not to follow the below-mentioned method - 

Here we form a list from the list-iterator that is returned when the ```zip()``` method is used. 

```python
    fruit_iterator = zip(fruit, dessert)
    fruit_dessert_list = list(fruit_iterator) # This creates a list of tuples 
    fruit_dessert_dictionary = dic(fruit_dessert_list)
```

:warning: The above method of creating a dictionary from a list is not efficient.

:warning: Also, if the size of the two lists are not same then the extra element will not be created in the dictionary.  

:warning: The list iterator type that is returned from the ```zip()``` method is exhaustable. If it is used once it cannot be used again. An example for the same is given below - 

```python
list_iterator = zip(list_1, list_2)
print(list(list_iterator)) # list_iterator has been used, hence it cannot be used again.
print(list(list_iterator)) # here an empty list will be printed as list iterator has already been used.
```

1.  **Dictionary to List conversion**

A dictionary can also be converted to a list. To convert a dictionary to a list, we make use of the ```items()``` method. We can also make use of the ```keys()``` and ```values()``` method.

Here is an exmaple - 

```python
fruit_desserts = {
    "watermelon" : "watermelon short cake",
    "mango" : "mango icecream sundae"
}
list = dictionary.items()

list = dictionary.values()
```

#### Sets and Frozensets

Sets allow us to store unique items, i.e. no duplicate items can be stored. If duplicate items are given to a set, set automatically removes them. Sets in python cannot mutable objects.

We can create sets in python in the following two ways - 

1.  **set() function**

    A set in python can be created by making use of the ```set()``` fuction. 
    
    Here is an example - 

    ```python
    watermelon = set('I love watermelons!')
    ```

    :warning: We can pass only pass immutable objects as a parameter in the ```set()``` function. If mutable objects are given as a parameter in the ```set()``` function, it will raise an error.

    Here is an example which shows the error raised if a mutable object is passed as a parameter in the set function - 

    ```python
    new_set = set((('watermelon', 'mango'), ('chilli', 'potato', 'lemon')))
    ```

1. **{} braces**

    After ```python 2.6```, sets can be created by just using the ```{} braces```. 
    
    Here is an example for the same - 

    ```python
    latest_set = {'apple', 'mango', 'banana', 'sapote'}
    ```

##### Frozensets

Frozensets are immutable sets. Sets are mutable, but frozensets are not. Frozensets can be created using the ```frozenset()``` method.

Here is an exmaple that shows it's usage - 

```python
new_frozen_set = frozenset(['apple', 'banana', 'mango', 'orange'])
```

#### Set Operations

Below mentioned are the operations that can be performed on sets - 

1.  **```add(element)```**

    The ```add(element)``` method can be used to add immutable objects to a list. However, if we try to add a mutable object to a list, an error will be raised.


    Here is an exmaple - 

    ```python
    fruit_set = {'apple', 'lychee', 'watermelon'}
    fruit_set.add('sapote')
    ```
    :warning: The below shown code will raise an error as a mutable object is being added to a set.

    ```python
    fruit_set.add(['watermelon', 'mango', 'sapote', 'lychee'])
    ```

1.  **```clear()```**

    The clear method removes all the elements from the set.

    Here is an example for the same - 

    ```python
    fruit_set.clear() 
    ```

1. **```copy()```**

    The ```copy()``` method shallow copies a set. 

    Here is an example - 

    ```python
    copied_set = fruit_set.copy() 
    ``` 

1. **```difference```**

    The ```difference()``` method finds the differnce between two sets. 

    Here is an example for the same - 

    ```python
    tasty_fruits = {'watermelon', 'mango', 'lychee', 'lemon'}
    super_tasty_fruits = {'watermelon', 'yellow-watermelon'}

    some_fruits = tasty_fruits.difference(super_tasty_fruits)
    ```

1.  **```difference_update()```**

    This method is similar to the ```difference()``` method, the only difference being that the result is stored in the same set. It is equivalent to ```x = x - y```. 

    Here is an example - 

    ```python
    x = {'a', 'b', 'c', 'd'}
    y = {'c', 'd'}
    x.difference_update(y)
    ``` 

1.  **```discard(element)```**

    This method is used to remove an element from the set. If the element specified in the function parameter is not present in the set then no error is raised.

    Here is an example - 

    ```python
    fruit_set.discard('melon')
    ```

1.  **```remove(element)```**

    The ```remove(element)``` method removes the specified element from the set. However, if the element specified is not present in the set then here an error is raised.

    Here is an example - 

    ```python
    fruit_set.remove('watermelon')
    ```  

    :warning: Here an error will be raised if the specified element in the ```remove(element)``` method is not present in the set.

1.  **```union(set)```**

    This method returns the union of two sets as a new set. 
    
    Here is an example

    ```python
    x = {'1', '2', '3'}
    y = {'a', 'b', 'c'}

    z = x.union(y)
    ```  

1.  **```intersection(set)```**

    This method is used find the intersection of two sets. 

    Here is an example - 

    ```python
    x = {'1', '2', '3'}
    y = {'a', 'b', 'c'}

    z = x.intersection(y)
    ```

1.  **```isdisjoint(set)```**

    This method is used to find whether two sets are ```disjoint``` or not. It returns  boolean value.

    Here is an example - 

    ```python
    truth_value = x.isdisjoint(y)
    ```

1. **```issubset()```**

    This method is used to check whether a given set is a subset of another set.

    Here is an example - 

    ```python
    x = {'1', '2', '3', 'a', 'c', 'b'}
    y = {'a', 'b', 'c'}
    
    print(x.issubset(y))
    ```

    Also, the following shortcuts can also be used to find whether a given set is a subset of another set - 

    1.  ```<=```

        The ```<=``` operator stands for ```is Subset of```. Here is an example - 

        ```python
        x = {'1', '2', '3', 'a', 'c', 'b'}
        y = {'a', 'b', 'c'}

        print(x <= y)
        ```

    1.  ```<```

        The ```<``` opertaor stands for ```is proper subset of```. This can be used in the following way - 

        ```python
        x = {'1', '2', '3', 'a', 'c', 'b'}
        y = {'a', 'b', 'c'}

        print(x < y)
        ```

    1. ```>=```

        The ```>=``` opertaor stands for ```is superset of```. This can be used in the following way - 

        ```python
        x = {'1', '2', '3', 'a', 'c', 'b'}
        y = {'a', 'b', 'c'}

        print(x >= y)
        ```

    1.  ```>```

        The ```>``` opertaor stands for ```is proper superset of```. This can be used in the following way - 

        ```python
        x = {'1', '2', '3', 'a', 'c', 'b'}
        y = {'a', 'b', 'c'}

        print(x > y)
        ```

1.  **```issuperset(set)```**

    This method is used to find the whether a given set is ```superset``` of another set or not.

    Here is an example - 

    ```python
    x = {'1', '2', '3', 'a', 'c', 'b'}
    y = {'a', 'b', 'c'}

    print(x.issupperset(y))    
    ```

1.  **```pop()```**

    This method removes and returns an arbitrary element from a given set.

    Here is an example - 

    ```python
    x = {1, 2, 4, 5, 7, 8}
    x.pop() 
    ```
