## Data Types in Python
'''
    - Data types are the classification/categorization of data items.
    - It represents the kind of value [ that tells what operations can be performed on a particular data ]
    - Since everything is an object in Python programming,
        - data types are actually classes and
        - variables are instances (objects) of these classes
'''


'''
    Following are the standard or built-in data types of Python:

    - **Numeric**
    - **Sequence Type**
    - **Boolean**
    - **Set**
    - **Dictionary**
'''

## Numeric
'''
    - In Python, numeric data type represents the data that has a numeric value.
    - A numeric value can be integer, floating number, or even complex number.
    - These values are defined as int, float, and complex classes in Python.
        - ***Integers***
            - ***Integer*** value is represented by int class.
            - It contains positive or negative whole numbers (without fractions or decimals).
            - In Python, there is no limit to how long an integer value can be.
        - ***Float***
            - ***Float*** value is represented by the float class.
            - It is a real number with a floating-point representation.
            - It is specified by a decimal point.
            - Optionally, the character e or E followed by a positive or negative integer may be appended to specify scientific notation.
        - ***Complex Numbers***
            - Complex number is represented by a complex class.
            - It is specified as *(real part) + (imaginary part)j*.
            - For example - 2+3j
'''
a = 5
print(type(a))

b = 5.0
print(type(b))

c = 5+3j
print(type(c))
'''
OUTPUT:
    <class 'int'>
    <class 'float'>
    <class 'complex'>
'''


## Sequence
'''
    - In Python, the sequence is the ordered collection of similar or different data types.
    - Sequences allow to store multiple values in an organized and efficient fashion.
        1. String
            - In python there is no character data type, a character is a string of length one.
            - Hence In Python, Strings are arrays of bytes representing Unicode characters.
            - A string is a collection of one or more characters put in a single quote, double-quote or triple quote.
                - Creating String with Triple Quotes allows multiple lines
            - It is represented by str class.

        Accessing elements of String
            - In Python, individual characters of a String can be accessed by using the method of Indexing.
            - Indexing allows negative address references to access characters from the back of the String,
            - e.g. -1 refers to the last character, -2 refers to the second last character and so on.
'''
String1 = 'Siva'
print(String1)
print(type(String1))

String2 = "Kumar"
print(String2)
print(type(String2))

String3 = '''
This is a Multi Line String
See the O/P to understand it better
'''
print(String3)
print(type(String3))

# To Access the 1st char in a String 
print(String3[0])
# To Access the lat char in a Stringf
print(String3[-1])
'''
OUTPUT:
        Siva
        <class 'str'>
        Kumar
        <class 'str'>

        This is a Multi Line String
        See the O/P to understand it better

        <class 'str'>




'''

'''
1. List
    - Lists are just like arrays, but are very flexible as the items can be of different data types
    - Lists are Ordered Collection of data
    - Lists in Python can be created using the square brackets `[]`.
    - **Accessing elements of List**
        - List items ca be accessed using Indexing
        - It allows Negative Indexing as well
'''
list = ["Geeks", 90, 55.2, 'String', ['list0', 'list1', "list2" ]]
print(list)
print(type(list))
print(list[0])
print(list[-1])
'''
OUTPUT:
        ['Geeks', 90, 55.2, 'String', ['list0', 'list1', 'list2']]
        <class 'list'>
        Geeks
        ['list0', 'list1', 'list2']
'''


'''
1. Tuple
    - Just like a list, tuple is also an ordered collection of Python objects.
    - The only difference between tuple and list is that tuples are immutable i.e. tuples cannot be modified after it is created.
    - It is represented by `tuple` class.
    - tuples are created by placing a sequence of values separated by ‘comma’ with or without the use of parentheses
    - Tuple Items can be Accessed using Indexing [ Negative indexing is allowed ]
'''

'''
Boolean 

        - Data type with one of the two built-in values, True or False
        - It is denoted by the class `bool`
        - **Note :** True and False with capital 'T' and 'F' are valid Booleans otherwise python will throw an error.

        
Set

        - In Python, [Set](https://www.geeksforgeeks.org/python-sets/) is an unordered collection of data types that is iterable, mutable, and has no duplicate elements.
        - The order of elements in a set is undefined
        - Creating
            - Sets can be created by using the built-in `set()` function with an iterable object or a sequence of items inside curly braces
        - Accessing
            - Set items cannot be accessed by referring to an index, since sets are unordered the items has no index.
            - But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using *in* keyword.

            
Dictionaries

        - Dictionary in Python is an unordered collection of data
        - Dictionary holds `key:value` pair
        - Creating
            - Dictionary can be created using curly `{}` braces
            - Keys must be unique, immutable & of any data type
            - Dictionary can also be created by the built-in function `dict()`
        - Accessing
            1. In order to access the items of a dictionary refer to its key name. Key can be used inside square brackets. 
            2. There is also a method called `get()` that will also help in accessing the element from a dictionary.
'''

## tuples
tuple1 = (123, 543.01, 'Kumar')
print(tuple1)
print(type(tuple1))
print(tuple1[0])
print(tuple1[-1])

## Set
set1 = set([1, 2, 'Geeks', 4, 'For', 6, 'Geeks']) 
print(set1)
print(type(set1))
for i in set1:
    print(i)

## Dictionary
Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]} 
print(Dict) 
print(type(Dict))
print(Dict['Name'])
print(Dict[1])
print(Dict.get(1))