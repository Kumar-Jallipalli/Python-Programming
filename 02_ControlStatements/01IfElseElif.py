## Control Flow Statements
'''
    - To Depict the Real-World Scenarios of Decision Making, we need to implement the same in Programming as well
    - Decision-making statements in programming languages decide the direction of the flow of program execution.
    - Hence, are called Control Flow Statements
    - In Python, if-else, elif statement is used for decision making.
'''

## If Statement
'''
    - `if` statement is the most simple decision-making statement
    - if a certain condition is true then a block of statement is executed otherwise not.
    - Syntax
                if condition:
                    # Statements to execute if
                    # condition is true
'''

i = 10
if (i > 5):
    print(i)


## if-else
'''
    - If the Condition is True, then `if` block will be executed
    - If the condition is false, then `else` block will be executed
    - Syntax
                if (condition):
                    # Executes this block if
                    # condition is true
                else:
                    # Executes this block if
                    # condition is false
'''

if (i > 15):
    print(i + " is Greater than 15")
else:
    print(i + " is lesser than 15")


'''
NOTE:
    - Nested if statements mean an if statement inside another if statement. 
'''


## **if-elif-else ladder**
'''
    - The if statements are executed from the top down.
    - As soon as one of the conditions controlling the `if` is true,
        - Then the statement associated with that `if` is executed,
        - and the rest of the ladder is bypassed.
    - If none of the conditions is true, then the final `else` statement will be executed
    - Syntax
                if (condition):
                    statement
                elif (condition):
                    statement
                .
                .
                else:
                    statement
'''

if (i == 10):
    print("i is 10")
elif (i == 15):
    print("i is 15")
elif (i == 20):
    print("i is 20")
else:
    print("i is not present")


## Shorthand's
'''
    - If there is only ONE Statement to be executed, then we can use Shorthand's
    - `if` Shorthand → `if condition: statement`
    - `if-else` shorthand → `<statement_when_True> if condition else <statement_when_False>`
'''

if (i < 30): print("i is less than 30")

print(True) if (i < 30) else print(False)