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
