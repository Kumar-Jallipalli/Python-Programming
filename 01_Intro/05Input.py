## How to take Input values from User..?
'''
    - To take input from the user we make use of a built-in function `*input()*`
        - `input()` → The function returns the user's input in the form of a string.
            - **there is one optional parameter - prompt → `input('prompt')`**
            - **prompt** - text displayed before the user input
    - We can also type cast this input to integer, float or string by specifying the input() function inside the type
        - **Typecasting the input to Float → `float(input())`**
        - **Typecasting the input to Integer → `int(input())`**
        - **Typecasting the input to String → `str(input())`**  [ ⇒ Default behavior ]
'''

int = int(input('Please Enter an Integer Value : '))
float  = float(input('Please Enter a Float Value : '))

print(int + float)

input = input('Please ENter anthing : ')
print(type(input))

'''
    Please Enter an Integer Value : 5
    Please Enter a Float Value : 0.33
    5.33
    Please ENter anthing : 5
    <class 'str'>
'''