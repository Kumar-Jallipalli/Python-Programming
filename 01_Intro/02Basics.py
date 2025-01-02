## Revision
'''
    - Python programs are not compiled, rather they are interpreted.
    - Python files are stored with the extension `".py”`
        - Extension tells us
            1. Describes which Programs can run/execute this file
            2. Describes the Logo if the file
'''

print("Hi, My name is Kumar Jallipalli.")


## How to Execute a Python file
'''
    We can execute/run a Python Program/File using the following command
            1. `python <file_name.py>`
            2. `py <file_name.py>`
'''

## Variables in Python
'''
    - Variables need not be declared first in python. [ Since they are Dynamically Typed ]
    - They can be used directly.
    - Variables in python are case-sensitive.
'''
a = 3
A = 4
print(a)
print(A)

## **Conditions in Python**
'''
    - Conditional output in python can be obtained by using `if-else` and `elif` [ else if in Python ] statements.
'''
if (a%2 == 0):
    print("a is a PRIME Number")
elif A%2 == 0:
    print("A is a Prime Number")
else:
    print("Neither 'a' nor 'A' is a Prime Number ")

## Points to be remembered
'''
        1. After `if` or `elif` there need not to be parenthesis `()`, It is Optional to use
        2. After `if` or `elif` or `else` conditions, There must be `:`
        3. Indentation must be maintained after the if, elif and else statements
'''


## **Functions in Python**
'''
    - A function in python is declared by the keyword `def` before the name of the function.
    - The return type of the function need not be specified explicitly in python.
    - The function can be invoked by writing the function name followed by the parameter list in the brackets.
'''

## Function Declaration
def isEven (a):
    if a%2 == 0:
        print( str(a) + " is EVEN")
    else:
        print( str(a) + " is ODD")
'''
    # Notice the indentation after function declaration
    # and if and else statements
'''

## Function Calling
isEven(3)