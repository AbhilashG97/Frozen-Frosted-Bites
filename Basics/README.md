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

1.  **Loops**
    Loops in python follow this syntax - 
    ```python
    for token in tokens:
    ````
    :warning:   To print items of a collection in single line, you have to do the following:

    ```python
    for(item in items)
        print(item, end=" ")
    ```

2.  **Strings**
    Strings are immutable in python. They can be enclosed in single, double, triple quotes.
    
    :warning:   Strings in triple quotes can be written in multiple lines.

    :warning:   Multiplication can also be performed on strings.

    ```python 
        print(".-." * 4)
    ```
3.  