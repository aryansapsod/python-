# Definitons and Examples of Conditional Statements in Python: if, elif, else   
# They allow your code to execute different blocks based on whether a condition is True or False.
# 1. if Statement
# The if statement checks a condition.
# If the condition is True, the code inside it runs.
# Syntax:
# if condition:
#     # code to execute if condition is True
age = 18

if age >= 18:
    print("You are eligible to vote.")  # Output: You are eligible to vote.
    
# 2. elif Statement
# The elif (else if) statement checks another condition if the previous if condition was False.
# You can have multiple elif statements.
# Syntax:

# if condition1:
#     # code to execute if condition1 is True
# elif condition2:
#     # code to execute if condition2 is True

marks = 85

# # Defination function():
#   A function in Python is a block of reusable code that performs a specific task.
# Instead of writing the same code again and again, you write it once inside a function and call it whenever needed.

def function():                           # Function definition starts with 'def' keyword
    if marks >= 90:
        print("Grade: A")
    elif marks >= 80:
        print("Grade: B")
        
function()  # Output: Grade: B            # Function call to execute the code inside the function

# 3. else Statement
# The else statement runs if none of the previous conditions were True.

def check_grade():                        # Another function definition
    if marks >= 90:
        print("Grade: A")
    elif marks >= 80:
        print("Grade: B")
    else:
        print("Grade: C")                  # Output: Grade: B
        
        
        
check_grade()  # Function call to execute the code inside the function
num =20
def check_number():                       # Function definition
    if num > 10 :
        print("Execution successful")
    else:
        print("Unsuccessful")
check_number()  # Function call to execute the code inside the function


def function1():
    age = int(input("Enter A Age :"))
    print(f"Your Age Is :{age}")
    
function1()

#  Three Types Of Function IN Python :

# 1. Built-in Functions: These are functions that are already defined in Python, like print(), len(), and type().
# 2. User-defined Functions: These are functions that you create yourself using the def keyword, like the function() and check_grade() examples above.
# 3. Ananymous Function (Lambda Functions): These are small, unnamed functions definied using the lambda keyword, often used for short operations.
def check_voter_eligiblity():
    age = int(input("Enter Your Age: "))
    if age >= 18:
        print("You are Eligible to Vote.")
    else:
        print("You are Not Eligible to Vote.")
        
check_voter_eligiblity()


#  1.Function Definition: 
#       A function is defined using the def keyword followed by the function name and parentheses ().
#  2.Function declaration: 
#       This is the process of defining a function, which includes specifying its name, parameters (if any),
#     and the block of code it will execute.
#  3.Function Call: 
#       To execute the code inside a function, you call it by using its name followed by parentheses ().

# 1. Function Definition Example:

def greet():
    print("Hello, welcome to Python functions!")
greet()  # Function Call Example

# 2. Function Declaration Example:

def add_numbers(a, b):
    return a + b    
result = add_numbers(5, 3)  # Function Call Example
print("Sum:", result)  # Output: Sum: 8

# 3. Function Call Example:
def multiply_numbers(x, y):
    return x * y
product = multiply_numbers(4, 6)  # Function Call Example
print("Product:", product)  # Output: Product: 24
# In summary, functions in Python help organize code into reusable blocks, making it easier to read, maintain, and debug.

#  () --> Parentheses are used in function definitions and calls to enclose parameters and arguments.

#  {} --> Curly braces are used to define dictionaries and sets in Python.

#  [] --> Square brackets are used to define lists and access elements by index.

#  <> --> Angle brackets are not commonly used in standard Python syntax but may appear in type hints or comparisons.

# In summary, functions in Python help organize code into reusable blocks, making it easier to read, maintain, and debug.
#  (), {}, [], and <> are different types of brackets used in Python for various purposes.

# They allow you to execute different code blocks depending on whether certain conditions are met.

# 4. Summary of Conditional Statements
# if, elif, and else statements help control the flow of your program based on conditions.
# They allow you to execute different code blocks depending on whether certain conditions are met.
print("Conditional Statements in Python: if, elif, else")
print("They allow you to execute different code blocks depending on whether certain conditions are met.")
# In summary, if, elif, and else statements help control the flow of your program based on conditions.
# They allow you to execute different code blocks depending on whether certain conditions are met.
print("Conditional Statements in Python: if, elif, else")




