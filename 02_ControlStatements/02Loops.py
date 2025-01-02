## while loop
'''
    - `while` loop is used to execute a block of statements repeatedly until a given condition is satisfied/true
    - And when the condition becomes false, the line immediately after the loop in the program is executed.
    - Syntax:
                while expression:
                    statement(s)

    - Using else statement with while loop
    - Syntax:
                while condition:
                    # execute these statements
                    # until the coondition is true
                else:
                    # execute these statements 
                    # when the condition becomes false
                
    - Single statement while block → while condition: statement
'''

#Python program to illustrate combining else with while
count = 0
while (count < 3):    
    count = count + 1
    print("Hello Geek")
else:
    print("In Else Block")


## for loop
'''
    - For loops are used for sequential traversal.
        - For example: traversing a list or string or array etc. In Python,
    - There is no C style for loop, i.e., for (i=0; i<n; i++).
    - There is `for in` loop which is similar to `for each` loop in other languages.
    - Syntax:
                for iterator_var in sequence:
                    statements(s)

    - `for` loop can be used to iterate over a range
    - `For` loops can iterate over any iterable object (example: List, Set, Dictionary, Tuple or String).
    - **Using else statement with for loops**
        - as there is no condition in `for` loop based on which the execution will terminate
        - so the `else` block will be executed immediately after `for` block finishes execution.
'''

# Python program to illustrate
# Iterating over range 0 to n-1
n = 4
for i in range(0, n):
    print(i)


# Python program to illustrate
# Iterating over a list
print("List Iteration")
l = ["geeks", "for", "geeks"]
for i in l:
    print(i)
     
# Iterating over a tuple (immutable)
print("\nTuple Iteration")
t = ("geeks", "for", "geeks")
for i in t:
    print(i)
     
# Iterating over a String
print("\nString Iteration")    
s = "Geeks"
for i in s :
    print(i)
     
# Iterating over dictionary
print("\nDictionary Iteration")   
d = dict() 
d['xyz'] = 123
d['abc'] = 345
for i in d :
    print("%s  %d" %(i, d[i]))
    
#Iterating over a set
print("\nSet Iteration")
set1 = {1,2,3,4,5,6}
for i in set1:
    print(i),



## How for loop works Internally..?
'''
                            # A simple for loop example
                            fruits = ["apple", "orange", "kiwi"]

                            for fruit in fruits:
                                print(fruit)

    Now with the help of the above example, let's dive deep and see what happens internally here.
            1. Make the list (iterable) an iterable object with help of the iter() function.
            2. Run an infinite while loop and break only if the StopIteration is raised.
            3. In the try block, we fetch the next element of fruits with the next() function.
            4. After fetching the element we did the operation to be performed with the element. (i.e print(fruit))

                            fruits = ["apple", "orange", "kiwi"]

                            # Creating an iterator object 
                            # from that iterable i.e fruits
                            iter_obj = iter(fruits)

                            # Infinite while loop
                            while True:
                            try:
                                # getting the next item
                                fruit = next(iter_obj)
                                print(fruit)
                            except StopIteration:
                                # if StopIteration is raised, 
                                # break from loop
                                break
'''