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