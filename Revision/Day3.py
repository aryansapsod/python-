#  Differences between identifier and Variable in Python:
# 1. Definition:
#    - An identifier is the name used to identify a variable, function, class, module, or other objects in Python.
#    - A variable is a named location in memory that stores a value which can be changed during program execution.  

# 2. Purpose:
#    - Identifiers are used to give meaningful names to various programming constructs,
#      making the code more readable and maintainable.
#    - Variables are used to hold data that can be manipulated and accessed throughout the program. 
print("Revision Day 3: Identifiers vs Variables in Python")

#  Rules for Identifiers in Python:
# 1. An identifier must start with a letter (A-Z, a-z) or an underscore (_).
# 2. The subsequent characters can be letters, digits (0-9), or underscores.
# 3. Identifiers are case-sensitive (e.g., myVar and myvar are different).
# 4. Identifiers cannot be the same as Python reserved keywords (e.g., if, else, while, etc.).
# 5. There are no length restrictions on identifiers, but it's advisable to keep them reasonable for readability.   
# Example of valid identifiers
my_variable = 10
_variable2 = 20
MyVar = 30  
# Example of invalid identifiers (uncommenting these will raise errors)
# 2variable = 40  # Starts with a digit
# my-variable = 50  # Contains a hyphen
# if = 60  # Reserved keyword
#  Differences between mutable and immutable data types in Python:

# 1. Definition:
#    - Mutable data types are those that can be changed or modified after their creation.
#    - Immutable data types are those that cannot be changed or modified after their creation.
# 2. Examples:
#    - Mutable data types: list, dict, set, bytearray
#    - Immutable data types: int, float, str, tuple, frozenset, bytes
# 3. Behavior:
#    - When you modify a mutable object, the original object is changed.
#    - When you modify an immutable object, a new object is created, and the original
#      object remains unchanged.
print("Mutable vs Immutable Data Types in Python")
# Example of mutable data type (list)
my_list = [1, 2, 3]
print("Original list:", my_list)
my_list.append(4)  # Modifying the list
print("Modified list:", my_list)
# Example of immutable data type (string)
my_string = "Hello"
print("Original string:", my_string)
new_string = my_string + ", World!"  # Creating a new string
print("New string:", new_string)
print("Original string after modification attempt:", my_string)
# In summary, identifiers are names used to identify programming constructs, while variables are named locations that store data.
# Mutable data types can be changed after creation, while immutable data types cannot be changed after creation.


# () - Functions:

# Functions are defined using the def keyword followed by the function name and parentheses.
# They can take parameters (inputs) and can return values (outputs) using the return statement.
num1 = 10

print(num1)

#  10

num2 = 20 

print(num2)

# 20

#  In Format F :

print(f"num1: {num1}")

# num1: 10

#  Addition :

print(f"num1 + num2 = {num1 + num2}") 

# initialization :

i = 10   # initialization

print(f"i: {i}")  # i: 10 output

i += 1   # incrementing by 1
print(f"i after incrementing by 1: {i}")  # i after incrementing by 1: 11 output

i -= 1   # decrementing by 1
print(f"i after decrementing by 1: {i}")  # i after decrementing by 1: 10 output
i *= 2   # multiplying by 2
print(f"i after multiplying by 2: {i}")  # i after multiplying by 2: 20 output


# Data Types in Python:
# python has several built-in data types, including:
# 1.Numeric Types: int,float,complex
i = 10  # int data type
print(f"i: {i}, Type of i: {type(i)}")  # i: 10, Type of i: <class 'int'>

j = 15.5  # float data type
print(f"j: {j}, Type of j: {type(j)}")  # j: 15.5, Type of j: <class 'float'>

k = 3 + 4j  # complex data type
print(f"k: {k}, Type of k: {type(k)}")  # k: (3+4j), Type of k: <class 'complex'>

# 2.sequence Types: List,tuple,range
my_list = [1, 2, 3, 4, 5]  # list data type
print(f"my_list: {my_list}, Type of my_list: {type(my_list)}") # my_list: [1, 2, 3, 4, 5], Type of my_list: <class 'list'>
my_tuple = (1, 2, 3, 4, 5)  # tuple data type
print(f"my_tuple: {my_tuple}, Type of my_tuple: {type(my_tuple)}") # my_tuple: (1, 2, 3, 4, 5), Type of my_tuple: <class 'tuple'>
my_range = range(1, 6)  # range data type

# 3.mapping type: Dict
my_dict = {'a': 1, 'b': 2, 'c': 3}  # dict data type
print(f"my_dict: {my_dict}, Type of my_dict: {type(my_dict)}") # my_dict: {'a': 1, 'b': 2, 'c': 3}, Type of my_dict: <class 'dict'> 

# 4.set Types: set, frozenset
my_set = {1, 2, 3, 4, 5}  # set data type
print(f"my_set: {my_set}, Type of my_set: {type(my_set)}") # my_set: {1, 2, 3, 4, 5}, Type of my_set: <class 'set'>

my_frozenset = frozenset([1, 2, 3, 4, 5])  # frozenset data type
print(f"my_frozenset: {my_frozenset}, Type of my_frozenset: {type(my_frozenset)}") # my_frozenset: frozenset({1, 2, 3, 4, 5}), Type of my_frozenset: <class 'frozenset'>

# 5.boolean Type: Bool
is_true = True  # bool data type
print(f"is_true: {is_true}, Type of is_true: {type(is_true)}") # is_true: True, Type of is_true: <class 'bool'>

# text Type: str (string)
a = "Aryan"  # str data type
print(f"a: {a}, Type of a: {type(a)}")  # a: Aryan, Type of a: <class 'str'>

# 6.bianary Types: bytes ,bytearray ,memoryview
bytes_data = b'Hello'  # bytes data type
print(f"bytes_data: {bytes_data}, Type of bytes_data: {type(bytes_data)}")
# bytes_data: b'Hello', Type of bytes_data: <class 'bytes'>
bytearray_data = bytearray(b'Hello')  # bytearray data type
print(f"bytearray_data: {bytearray_data}, Type of bytearray_data: {type(bytearray_data)}")
# bytearray_data: bytearray(b'Hello'), Type of bytearray_data: <class 'bytearray'>
memoryview_data = memoryview(b'Hello')  # memoryview data type
print(f"memoryview_data: {memoryview_data}, Type of memoryview_data: {type(memoryview_data)}")
# memoryview_data: <memory at 0x...>, Type of memoryview_data: <class 'memoryview'>

# 7.complex Type: complex
complex_num = 3 + 4j  # complex data type
print(f"complex_num: {complex_num}, Type of complex_num: {type(complex_num)}")  # complex_num: (3+4j), Type of complex_num: <class 'complex'>

# Each data Type has its own characteristics and use cases.
print("Data Types in Python:")


# if :
# if, elif, and else — Explanation with Examples (Python)

# These are conditional statements used to make decisions in a program. 
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
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")  # Output: Grade: B   
    
# 3. else Statement
# The else statement runs if none of the previous conditions were True.

if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
else:
    print("Grade: C")  # Output: Grade: B
    
num =20 

if num > 10 :
    print("Exicution successful")
    
else:
    print("Unsuccessful")


Age = int(input("Enter your age: ")) 

if Age < 20:
    print("Voter Can Eligible")
    
else :
    print("Voter is Not Eligible")
    

