## **What is the maximum possible value of an integer in Python ?**
'''
    - ***In Python, value of an integer is not restricted by the number of bits and can expand to the limit of the available memory***
    - In Python, there is no limit to how long an integer value can be.
    - In Python 2.7. there are two separate types "int" (which is 32 bit) and "long int”
    - But from Python 3, there is only one type "int" for all type of integers
'''
x = 10000000000000000000000000000000000000000000
x = x + 1
print (x)
''' o/p : 10000000000000000000000000000000000000000001  '''


'''
**Python Operators** are used to perform operations on values and variables. 
        - An `operator` is **a symbol or sign that specifies the type of Operation/Calculation**
        - An `OPERAND` is the value on which the operator is applied.

    - In Python 3.x the result of division is a floating-point
    - while in Python 2.x division of 2 integer was an integer
    - To obtain an integer result in Python 3.x floored ( `//` integer) is used.

    Operator	Description	                                                                        Syntax
    +	        Addition: adds two operands	                                                        x + y
    -	        Subtraction: subtracts two operands	                                                x - y
    *	        Multiplication: multiplies two operands	                                            x * y
    /	        Division (float): divides the first operand by the second	                        x / y
    //	        Division (floor): divides the first operand by the second	                        x // y
    %	        Modulus: returns the remainder when the first operand is divided by the second	    x % y
    **	        Power: Returns first raised to power second	                                        x ** y
'''


## **Difference between == and is operator in Python**
'''
    - The Equality operator (`==`) is a comparison operator, that compare values of both the operands
    - Whereas the **`is`** operator is the  identity operator that checks whether both the operands refer to the same object or not 
        i.e., present in the same memory location or NOT.
    💡
    - `id()` function is used to returns the “identity” of an object.

'''

list1 = []
list2 = []

print(id(list1))
print(id(list2))

print(list1 == list2)
print(list1 is list2)

'''
OUTPUT:
    2015926903104
    2015927051264
    True
    False
'''