# Python basics

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


### Indentation 

A block is a group of statements in a program or script. Usually it consists of at least one statement and of declarations for the block, depending on the programming or scripting language. A language, which allows grouping with blocks, is called a **block structured language**.

```Python``` programs get structured through indentation, i.e. code blocks are defined by their indentation. All statements with the same distance to the right belong to the same block of code, i.e. the statements within a block line up vertically.

### Variables and Data Types 

**id Function**

The ```id()``` function can be used to uniquely identify variables in python. Every variable, object has a unique id associated with it.

:warning:   Data in a Python program is represented by objects.
            The objects can be - 
            1.  built-in, i.e. objects provided by Python
            1.  objects from extension libraries  
            1.  created in the application by the programmer.

**Literals**

Python's build-in core data-type is also called object type.

There are four built-in types for numbers - 

1. Normal Integers
1. Octal Literals (0o21)
1. Hexadecimal Literal (0x1A)
1. Binary Literal (0b001010)

:warning: bin(), hex(), and oct() functions can be used to create binary numbers for a given integer.

:warning: Integers in Python3 can be of **unlimited size**.

:exclamation:   There is no "long int" in Python3 anymore. There is only one "int" type, which contains both "int" and "long" from Python2

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
