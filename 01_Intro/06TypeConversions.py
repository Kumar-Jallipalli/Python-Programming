## Type Conversion
'''
    Type Conversion → Conversion of One Data Type to Another

    There are two types of Type Conversion in Python:
    1. Implicit Type Conversion → the Python interpreter automatically converts one data type to another without any user involvement.
    2. Explicit Type Conversion → the data type is manually changed by the user as per their requirement.
'''

## Type Conversion Functions
'''
    1. **`int(a,** **base)**`: This function converts **any data type to integer**.
                            'Base' specifies the base in which string is if the data type is a string.
    2. **`float()`**: This function is used to convert **any data type to a** floating-point **number.** 
    3. **`ord()` :** This function is used to convert a **character to integer.**
    4. **`hex()` :** This function is to convert **integer to hexadecimal string**.
    5. **`oct()` :** This function is to convert **integer to octal string**.
    6. **`tuple()` :** This function is used to **convert to a tuple**
    7. **`set()` :** This function returns the **type after converting to set**
    8. **`list()` :** This function is used to convert **any data type to a list type**.
    9. **`dict()` :** This function is used to **convert a tuple of order (key,value) into a dictionary**.
    10. **`str()` :** Used to **convert integer into a string.**
    11. **`complex(real,imag)` :** This function **converts real numbers to complex(real,imag) number.**
    12. **`chr(number)`:** This function **converts number to its corresponding ASCII character.**
'''

## Implicit Conversion
x = 5
y = 5.5
z = x+y
print(z)
print(type(z))

## Explicit COnversion
s = "10100"

i = int(s, 2)
print(i)
print(type(i))

f = float(s)
print(f)
print(type(f))

t = tuple(s)
print(t)
print(type(t))

c = set(s)
print(c)
print(type(c))

l = list(s)
print(l)
print(type(l))

comp = complex(1, 2)
print(comp)
print(type(comp))

tup = (('a', 1), ('b', 2), ('c', 3))
d = dict(tup)
print(d)
print(type(d))

print(chr(76))
print(ord('a'))
print(hex(76))
print(oct(76))

'''
    10.5
    <class 'float'>
    20
    <class 'int'>
    10100.0
    <class 'float'>
    ('1', '0', '1', '0', '0')
    <class 'tuple'>
    {'0', '1'}
    <class 'set'>
    ['1', '0', '1', '0', '0']
    <class 'list'>
    (1+2j)
    <class 'complex'>
    {'a': 1, 'b': 2, 'c': 3}
    <class 'dict'>
    L
    97
    0x4c
    0o114
'''
