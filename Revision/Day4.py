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



