# Document String :
# A docstring is a string literal that appears as the first statement in a module, function, class, or method definition.
# It provides documentation for the code and can be accessed using the __doc__ attribute.
# Docstrings are used to explain what a function does, its parameters, and its return value.

def example_function():
    """
    This function demonstrates how to use docstrings.
    It takes no arguments and returns nothing.
    """
    print("Hey! , I Am Your Aryan")

print(example_function.__doc__)
example_function()

# Output:
# This function demonstrates how to use docstrings.
# It takes no arguments and returns nothing.

# In summary, docstrings are a way to document your code, making it easier for others (and yourself) to understand its purpose and usage.

#  Functions In Python :
# Functions are reusable blocks of code that perform a specific task.
# They help organize code, make it more readable, and allow for code reuse.
def greet():
    """This function greets the user."""
    print("Hello I Am Aryan, Welcome to Python functions!")
greet()  # Function call to execute the code inside the function
print(greet.__doc__)


# Types Of Functions In Python :

# Parameterless Function: A function that does not take any parameters.
def say_hello():
    print("Hello, Aryan!")
    
say_hello()

# Parameterized Function: A function that takes parameters to perform its task.
def greet_user(name):
    print(f"Hello, {name}!")
greet_user("Aryan")

num1 = 20
num2 = 30

def function():    # Def = Denifine function
    print("inside  Parameterless Function")       #In Blocks 
    print(f"num1 + num2= {num1+num2}")
    
    
function()      # Function Call


    

# Function with Return Value: A function that returns a value after performing its task.
def add_numbers(a, b):
    return a + b
result = add_numbers(5, 3)
print(f"Sum: {result}")
# Recursive Function: A function that calls itself to solve a problem.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
fact = factorial(5)
print(f"Factorial: {fact}")
# Lambda Function: A small anonymous function defined using the lambda keyword.
square = lambda x: x * x
print(f"Square: {square(4)}")

