# Variables
# Variables are used to store data values
# In Python, variables do not need to be declared with any particular type and can even change type after they have been set.
# Variables can be assigned values using the assignment operator (=)
# Example:
x = 5
y = "Hello, World!"
z = 3.14
# print(x) # Output: 5
# print(y) # Output: Hello, World!
# print(z) # Output: 3.14
# print(type(x)) # Output: <class 'int'>
# print(type(y)) # Output: <class 'str'>
# print(type(z)) # Output: <class 'float'>

# Python has no command for declaring a variable.
# A variable is created the moment you first assign a value to it.

# Operators
# Python has the following types of operators:
# Arithmetic operators: +, -, *, /, %, **, //
# Comparison operators: ==, !=, >, <, >=, <=
# Logical operators: and, or, not
# Assignment operators: =, +=, -=, *=, /=, %=, **=, //=
# Identity operators: is, is not
# Membership operators: in, not in
# Bitwise operators: &, |, ^, ~, <<, >>
# Example:
a = 10
b = 3
print(a + b)  # Addition: 13
print(a - b)  # Subtraction: 7
print(a * b)  # Multiplication: 30
print(a / b)  # Division: 3.3333
print(a // b) # Floor Division: 3
print(a % b)  # Modulus: 1
print(a ** b) # Exponentiation: 1000

## Comparison Operators (Return True or False)

x = 10
y = 20
print(x > y)  # False
print(x < y)  # True
print(x == y) # False
print(x != y) # True


## Logical Operators (and, or, not)


x = True
y = False
print(x and y)  # False
print(x or y)   # True
print(not x)    # False


## Assignment Operators

x = 10
x += 5  # Equivalent to: x = x + 5
x *= 2  # Equivalent to: x = x * 2
print(x)  # Output: 30

## Identity Operators (is, is not)
x = [1, 2, 3]
y = x
z = x.copy()   # z is a copy of x, not the same object  creates a shallow copy of the list
print(x is y)  # True (y is the same object as x)
print(x is z)  # False (z is a copy of x)

 ## Membership Operators (in, not in)

fruits = ["apple", "banana", "cherry"]
print("apple" in fruits)   # True
print("grape" not in fruits)  # True

## Bitwise Operators
# Bitwise operators are used to perform bit-level operations on integers.
# They work on bits and perform bit-by-bit operations.
# Example:
# & (AND), | (OR), ^ (XOR), ~ (NOT), << (Left Shift), >> (Right Shift)
# Example:
a = 5  # 0101 in binary
b = 3  # 0011 in binary
print(a & b)  # Bitwise AND: 1 (0001 in binary)
print(a | b)  # Bitwise OR: 7 (0111 in binary)
print(a ^ b)  # Bitwise XOR: 6 (0110 in binary)
print(~a)     # Bitwise NOT: -6 (inverts all bits)
print(a << 1) # Left Shift: 10 (1010 in binary)
print(a >> 1) # Right Shift: 2 (0010 in binary)


# Strings
# Strings are sequences of characters enclosed in quotes (single or double).
# Strings can be manipulated using various methods and operators.
# Example:
string1 = "Hello"
string2 = 'World'
string3 = """This is a multi-line string." \
"""
string4 = '''This is another multi-line string.'''
print(string1)  # Output: Hello
print(string2)  # Output: World
print(string4)  # Output: This is another multi-line string.
print(string3)  # Output: This is a multi-line string.
print(type(string1))  # Output: <class 'str'>
print(type(string2))  # Output: <class 'str'>
print(type(string3))  # Output: <class 'str'>
print(type(string4))  # Output: <class 'str'>
print(len(string1))  # Output: 5 (length of the string)
print(string1 + " " + string2)  # Concatenation: Hello World
print(string1 * 3)  # Repetition: HelloHelloHello
print(string1[0])  # Indexing: H (first character)
print(string1[1:4])  # Slicing: ell (characters from index 1 to 3)
print(string1.lower())  # Lowercase: hello
print(string1.upper())  # Uppercase: HELLO
print(string1.replace("H", "J"))  # Replace: Jello
print(string1.split("l"))  # Split: ['He', '', 'o']
print("Hello".join(string1))  # Join: HHello
print("Hello" in string1)  # Membership: True
print("Hello" not in string1)  # Membership: False
print(string1.strip())  # Strip: Hello (removes leading and trailing whitespace)
print(string1.startswith("H"))  # Starts with: True
print(string1.endswith("o"))  # Ends with: True
print(string1.capitalize())  # Capitalize: Hello
print(string1.title())  # Title case: Hello
print(string1.find("l"))  # Find: 2 (index of first occurrence of 'l')
print(string1.count("l"))  # Count: 2 (number of occurrences of 'l')
print(string1.isalnum())  # Alphanumeric: True (contains only letters and numbers)
print(string1.isalpha())  # Alphabetic: True (contains only letters)
print(string1.isdigit())  # Digit: False (contains non-digit characters)
print(string1.islower())  # Lowercase: False (contains uppercase characters)
print(string1.isupper())  # Uppercase: False (contains lowercase characters)
print(string1.isspace())  # Space: False (contains non-space characters)
print(string1.title())  # Title case: Hello
print(string1.swapcase())  # Swap case: hELLO

print(string1.center(10))  # Center: '  Hello   ' (padded with spaces to a total width of 10)
print(string1.ljust(10))  # Left justify: 'Hello     ' (padded with spaces to a total width of 10)
print(string1.rjust(10))  # Right justify: '     Hello' (padded with spaces to a total width of 10)
print(string1.zfill(10))  # Zero fill: '00000Hello' (padded with zeros to a total width of 10)
print(string1.expandtabs(4))  # Expand tabs: 'Hello' (replaces tabs with spaces, default tab size is 8)
print(string1.splitlines())  # Split lines: ['Hello'] (splits the string into a list of lines)
print(string1.partition("l"))  # Partition: ('He', 'l', 'lo') (splits the string into a tuple of three parts)

# String Formatting
# String formatting allows you to create strings with dynamic content.
# There are several ways to format strings in Python:
# 1. Using the format() method
# 2. Using f-strings (formatted string literals)
# 3. Using the % operator (old-style formatting)
# 4. Using the str.format() method (new-style formatting)
# Example:
name = "John"
age = 30
height = 1.75
# Using the format() method
formatted_string1 = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string1)  # Output: My name is John and I am 30 years old.

# Using f-strings (Python 3.6+)
formatted_string2 = f"My name is {name} and I am {age} years old."
print(formatted_string2)  # Output: My name is John and I am 30 years old.

# Using the % operator (old-style formatting)
formatted_string3 = "My name is %s and I am %d years old." % (name, age)
print(formatted_string3)  # Output: My name is John and I am 30 years old.


# Using the str.format() method (new-style formatting)
formatted_string4 = "My name is {0} and I am {1} years old.".format(name, age)
print(formatted_string4)  # Output: My name is John and I am 30 years old.

# Using the str.format() method with named placeholders
formatted_string5 = "My name is {name} and I am {age} years old.".format(name=name, age=age)
print(formatted_string5)  # Output: My name is John and I am 30 years old.


# Using the str.format() method with positional and keyword arguments
formatted_string6 = "My name is {0} and I am {age} years old.".format(name, age=age)
print(formatted_string6)  # Output: My name is John and I am 30 years old.

# Using the str.format() method with formatting options
formatted_string7 = "My name is {0} and I am {1:.2f} years old.".format(name, height)
print(formatted_string7)  # Output: My name is John and I am 1.75 years old.

#Control flow
# Control flow statements are used to control the execution of code based on certain conditions.
# Python has the following control flow statements: 
# if, elif, else, for, while, break, continue, pass
# Example:
# if statement
x = 10
y = 20
if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("x is equal to y")
# Output: x is less than y


# for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Output:
# apple
# banana
# cherry

# while loop
count = 0
while count < 5:
    print(count)
    count += 1
# Output:
# 0
# 1
# 2
# 3
# 4

# break statement
count = 0
while count < 5:
    if count == 3:
        break
    print(count)
    count += 1
# Output:
# 0
# 1
# 2


# continue statement
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue
    print(count)
# Output:
# 1
# 2
# 4
# 5

# pass statement
count = 0
while count < 5:
    count += 1
    if count == 3:
        pass  # Do nothing
    print(count)

# Output:
# 1
# 2
# 3
# 4
# 5

# Input and Output
# Input and output functions are used to read data from the user and display data to the user.
# Python has the following input and output functions:
# input(), print()
# Example:
# Input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Hello, {}! You are {} years old.".format(name, age))
# Output: Hello, John! You are 30 years old.
# Note: The input() function returns a string, so we need to convert it to an integer using int() for age.
# You can also use float() to convert to a float if needed.
# Example:
height = float(input("Enter your height: "))
print("Your height is {} meters.".format(height))
# Output: Your height is 1.75 meters.
# Note: The input() function will wait for the user to enter data and press Enter.
# The entered data will be stored in the variable name.
# The int() function converts the input string to an integer.
# The print() function displays the output to the console.
# The format() method is used to format the string with the values of name and age.
# The {} placeholders in the string will be replaced with the values of name and age.
# The output will be displayed in the console.
# The print() function can also take multiple arguments separated by commas.
# Example:
print("Hello", name, "You are", age, "years old.")
# Output: Hello John You are 30 years old.
# Note: The print() function automatically adds a space between the arguments.

# You can also use the sep parameter to specify a different separator.
# Example:
print("Hello", name, "You are", age, "years old.", sep=", ")
# Output: Hello, John, You are, 30, years old.

# Note: The sep parameter specifies the separator between the arguments.
# The default separator is a space.
# You can change it to any string you want.
# Example:
print("Hello", name, "You are", age, "years old.", sep="|")
# Output: Hello|John|You are|30|years old.


# You can also use the end parameter to specify a different ending character.
# Example:
print("Hello", name, "You are", age, "years old.", end=".")
# Output: Hello John You are 30 years old.
# Note: The end parameter specifies the ending character.
# The default ending character is a newline (\n).
# You can change it to any string you want.
# Example:
print("Hello", name, "You are", age, "years old.", end="|")
# Output: Hello John You are 30 years old.|



# You can also use the flush parameter to specify whether to flush the output buffer or not.
# Example:
print("Hello", name, "You are", age, "years old.", flush=True)
# Output: Hello John You are 30 years old.
# Note: The flush parameter specifies whether to flush the output buffer or not.
# The default value is False.
# You can change it to True to flush the output buffer immediately.
# This is useful when you want to see the output immediately without waiting for the buffer to fill up.



# Functions
# Functions are reusable blocks of code that perform a specific task.
# Functions can take input parameters and return output values.
# Python has built-in functions and user-defined functions.
# Example:
# Built-in function

## Build In functions

print(len("Hello"))  # Output: 5
print(max([1, 5, 3, 9]))  # Output: 9
print(sum([1, 2, 3]))  # Output: 6

## User defined

def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!

# ✔ With Default Parameters

def greet(name="Guest"):
    return f"Hello, {name}!"

print(greet())  # Output: Hello, Guest!

# ✔ With Multiple Arguments

def add(a, b):
    return a + b

print(add(5, 3))  # Output: 8

# ✔ With Variable Arguments (*args & **kwargs)

def multiply(*args):  # Accepts multiple positional arguments
    result = 1
    for num in args:
        result *= num
    return result

print(multiply(2, 3, 4))  # Output: 24

def student_info(**kwargs):  # Accepts multiple keyword arguments
    return kwargs

print(student_info(name="Alice", age=20, grade="A"))
# Output: {'name': 'Alice', 'age': 20, 'grade': 'A'}

# Note: The *args parameter allows you to pass a variable number of positional arguments to the function.
# The **kwargs parameter allows you to pass a variable number of keyword arguments to the function.
# You can use either or both of these parameters in your function definition.
# The *args parameter collects all the positional arguments into a tuple.
# The **kwargs parameter collects all the keyword arguments into a dictionary.
# You can then access the arguments using indexing or key-value pairs.

# Lambda Functions
# Lambda functions are anonymous functions that can take any number of arguments but can only have one expression.
# They are often used for short, throwaway functions.
# Example:
add = lambda x, y: x + y
print(add(5, 3))  # Output: 8


#Syntax of a Lambda Function in Python
#A lambda function is a small anonymous function that can have multiple arguments but only one expression.

#Syntax:


#lambda arguments: expression
#lambda → Keyword to define the function.
#arguments → Input parameters (like a normal function).
#expression → A single expression that gets evaluated and returned.
#x1f539; Examples of Lambda Functions
#Basic Example


square = lambda x: x * x
print(square(5))  # Output: 25
#Lambda with Multiple Arguments

add = lambda a, b: a + b
print(add(3, 7))  # Output: 10AC
#Using Lambda with map()

nums = [1, 2, 3, 4]
squared_nums = list(map(lambda x: x ** 2, nums))
print(squared_nums)  # Output: [1, 4, 9, 16]
#Using Lambda with filter()

nums = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # Output: [2, 4]
#Using Lambda with sorted()

students = [("Alice", 25), ("Bob", 22), ("Charlie", 23)]
students.sort(key=lambda x: x[1])  # Sort by age
print(students)
# Output: [('Bob', 22), ('Charlie', 23), ('Alice', 25)]


#Key Features of Lambda Functions
#Single expression only (no multiple statements).
#Useful for short, simple functions.
#Can be used inside map(), filter(), and sorted() functions.
#Anonymous (no function name required).


#Recursive Functions
# A recursive function is a function that calls itself to solve a problem.
# Recursive functions are used to solve problems that can be broken down into smaller subproblems.
# Example:
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# Test the recursive function
print(factorial(5))  # Output: 120


# Higher-Order Functions
# Higher-order functions are functions that can take other functions as arguments or return functions as results.
# They are used to create more flexible and reusable code.
# Example:
def apply_function(func, value):
    return func(value)

nums = [1, 2, 3, 4, 5]

# Using map() to square numbers
squared = list(map(lambda x: x * x, nums))
print(squared)  # Output: [1, 4, 9, 16, 25]

# Using filter() to get even numbers
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # Output: [2, 4]

# Inner nested functions
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

# Generator functions
def countdown(n):
    while n > 0:
        yield n
        n -= 1

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

gen = fibonacci_generator()
for _ in range(5):
    print(next(gen), end=" ")  # Output: 0 1 1 2 3


def even_numbers(limit):
    num = 0
    while num <= limit:
        yield num
        num += 2

evens = even_numbers(10)
print(list(evens))  # Output: [0, 2, 4, 6, 8, 10] 


def water_dispenser():
    yield "Cup 1 of water"
    yield "Cup 2 of water"
    yield "Cup 3 of water"
    yield "Cup 4 of water"

# Using the generator
dispenser = water_dispenser()

# Getting water (values) one at a time
print(next(dispenser))  # "Cup 1 of water"
print(next(dispenser))  # "Cup 2 of water"
print(next(dispenser))  # "Cup 3 of water"
print(next(dispenser))  # "Cup 4 of water"


### Using the generator in a loop
for cup in water_dispenser():
    print(cup)
# Output:
# Cup 1 of water
# Cup 2 of water
# Cup 3 of water
# Cup 4 of water

# Decorators
# Decorators are a way to modify or enhance functions or methods without changing their code.
# They are often used to add functionality to existing functions or methods.
# Decorators are defined using the @ symbol followed by the decorator function name.
# Example:
def decorator_function(func):
    def wrapper_function():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper_function


@decorator_function
def say_hello():
    print("Hello, World!")



say_hello()
# Output:
# Before the function call
# Hello, World!
# After the function call

# Note: The @decorator_function syntax is a shorthand for say_hello = decorator_function(say_hello).
# It applies the decorator_function to the say_hello function, modifying its behavior.


# Decorators with Arguments
def decorator_with_args(arg1, arg2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Decorator arguments: {arg1}, {arg2}")
            return func(*args, **kwargs)
        return wrapper
    return decorator


@decorator_with_args("Hello", "World")
def greet(name):
    print(f"Hello, {name}!")


greet("Alice")
# Output:
# Decorator arguments: Hello, World
# Hello, Alice!
# Note: The decorator_with_args function takes arguments and returns a decorator function.
# The inner wrapper function can access the arguments passed to the decorator.
# This allows you to create more flexible decorators that can accept parameters.

# Decorators with Return Values
def decorator_with_return_value(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"Decorated result: {result}"
    return wrapper


@decorator_with_return_value
def add(a, b):
    return a + b


print(add(5, 3))  # Output: Decorated result: 8
# Note: The decorator_with_return_value function modifies the return value of the decorated function.
# The wrapper function calls the original function and modifies its return value before returning it.
# This allows you to create decorators that can change the output of the decorated function.


# Packages and Modules
# Packages and modules are used to organize and structure Python code into reusable components.
# A module is a single file containing Python code, while a package is a directory containing multiple modules and an __init__.py file.
# Example:
#### Importing using builtin modules

import math

print(math.sqrt(16))  # Output: 4.0
print(math.pi)        # Output: 3.141592653589793
print(math.factorial(5))  # Output: 120

import random

print(random.randint(1, 10))  # Random number between 1 and 10
print(random.choice(["apple", "banana", "cherry"]))  # Random choice


import math as m

print(m.sqrt(25))  # Output: 5.0
print(m.pi)        # Output: 3.141592653589793

## 🔹 3️⃣ Importing Specific Functions from a Module

from math import sqrt, pi

print(sqrt(49))  # Output: 7.0
print(pi)        # Output: 3.141592653589793

## 🔹 4️⃣ Importing All Functions from a Module
## You can import everything from a module using *, but it's not recommended (can cause conflicts).

from math import *

print(sin(pi/2))  # Output: 1.0
print(factorial(4))  # Output: 24


# Note: The import statement allows you to use functions and variables defined in other modules.
# You can import built-in modules, third-party modules, or your own custom modules.

### 📌 2. Creating Your Own Module

# my_module.py
def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b


import my_module

print(my_module.greet("Alice"))  # Output: Hello, Alice!
print(my_module.add(5, 3))  # Output: 8

# ✅ Using __name__ == "__main__" in a Module
# If a module is run directly, __name__ is "__main__". This prevents certain code from executing when the module is imported elsewhere.

def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet("Alice"))  # This runs only when executed directly


# Note: The __name__ variable is a built-in variable that indicates the name of the module.
# If the module is run directly, __name__ is set to "__main__".
# If the module is imported, __name__ is set to the module's name.
# This allows you to write code that should only run when the module is executed directly, not when it's imported.
# This is useful for testing or running specific code when the module is executed as a script.
# This is a common practice in Python programming to avoid executing certain code when the module is imported elsewhere.
# It allows you to define functions and classes in a module while preventing certain code from running when the module is imported.



# Exception Handling
# Exception handling is used to handle errors and exceptions that may occur during program execution.
# Python has the following exception handling statements:
# try, except, finally, raise
# Example:
try:
    x = 10 / 0  # Division by zero error
except ZeroDivisionError:
    print("Error: Division by zero!")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("This block always executes.")
# Output:
# Error: Division by zero!
# This block always executes.

# Note: The try block contains the code that may raise an exception.
# The except block contains the code to handle the exception.
# You can have multiple except blocks to handle different types of exceptions.
# The finally block contains code that always executes, regardless of whether an exception occurred or not.
# This is useful for cleanup operations, such as closing files or releasing resources.
# The raise statement is used to raise an exception manually.
# Example:
try:
    raise ValueError("This is a custom error message.")
except ValueError as e:
    print(f"Custom error: {e}")
# Output:
# Custom error: This is a custom error message.
# Note: The raise statement can be used to raise built-in exceptions or custom exceptions.
# You can also raise exceptions with custom error messages to provide more context about the error.
# This is useful for debugging and error handling.
# You can also create custom exception classes by subclassing the built-in Exception class.
# Example:
class CustomError(Exception):
    pass


try:
    raise CustomError("This is a custom error.")
except CustomError as e:
    print(f"Custom error: {e}")
# Output:
# Custom error: This is a custom error.
# Note: Custom exception classes allow you to define your own error types and handle them separately.
# This is useful for creating more specific error handling in your code.

# Data Structures
# Python has built-in data structures that allow you to store and manipulate collections of data.
# The most common data structures in Python are:
# lists, tuples, sets, and dictionaries.
# Example:
# Lists
# Lists are ordered collections of items that can be changed (mutable).
# Lists can contain items of different types.
# Lists are defined using square brackets [] and can be indexed and sliced.
# Example:
fruits = ["apple", "banana", "cherry"]
print(fruits)  # Output: ['apple', 'banana', 'cherry']
print(fruits[0])  # Output: apple
print(fruits[1:3])  # Output: ['banana', 'cherry']
print(fruits[-1])  # Output: cherry (last item)
print(fruits[1:])  # Output: ['banana', 'cherry'] (from index 1 to the end)
print(fruits[:2])  # Output: ['apple', 'banana'] (from the beginning to index 2)
print(fruits[::2])  # Output: ['apple', 'cherry'] (every second item)
print(fruits[::-1])  # Output: ['cherry', 'banana', 'apple'] (reversed list)
print(fruits[1:3])  # Output: ['banana', 'cherry'] (from index 1 to 2)



# List Methods
# Lists have several built-in methods for manipulation.
# Example:
fruits.append("orange")  # Add an item to the end of the list
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']

fruits.insert(1, "kiwi")  # Insert an item at a specific index
print(fruits)  # Output: ['apple', 'kiwi', 'banana', 'cherry', 'orange']


fruits.remove("banana")  # Remove an item by value
print(fruits)  # Output: ['apple', 'kiwi', 'cherry', 'orange']


fruits.pop(2)  # Remove an item by index and return it
print(fruits)  # Output: ['apple', 'kiwi', 'orange']


fruits.sort()  # Sort the list in ascending order
print(fruits)  # Output: ['apple', 'kiwi', 'orange']


fruits.reverse()  # Reverse the order of the list
print(fruits)  # Output: ['orange', 'kiwi', 'apple']



fruits.clear()  # Remove all items from the list
print(fruits)  # Output: [] (empty list)


# List Comprehensions
# List comprehensions are a concise way to create lists using a single line of code.
# They are often used for transforming or filtering data.
# Example:
squared_numbers = [x ** 2 for x in range(10)]
print(squared_numbers)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)  # Output: [0, 2, 4, 6, 8]

# Note: List comprehensions are a powerful feature in Python that allows you to create lists in a more readable and efficient way.
# They can replace traditional for loops for creating lists and can improve code readability.
# List comprehensions can also be used with nested loops and conditional statements.
# Example:
nested_list = [[x, y] for x in range(3) for y in range(2)]
print(nested_list)  # Output: [[0, 0], [0, 1], [1, 0], [1, 1], [2, 0], [2, 1]]
# Note: The nested list comprehension creates a list of lists using two nested loops.
# It generates all combinations of x and y values in the specified ranges.
# This is useful for creating multidimensional lists or matrices.
# You can also use list comprehensions with functions and methods.
# Example:
fruits = ["apple", "banana", "cherry"]
fruits_upper = [fruit.upper() for fruit in fruits]
print(fruits_upper)  # Output: ['APPLE', 'BANANA', 'CHERRY']
# Note: The list comprehension applies the upper() method to each fruit in the list, creating a new list with uppercase fruit names.
# This is useful for transforming data in a concise way.
# You can also use list comprehensions with dictionaries and sets.
# Example:
fruits = ["apple", "banana", "cherry"]
fruits_dict = {fruit: len(fruit) for fruit in fruits}
print(fruits_dict)  # Output: {'apple': 5, 'banana': 6, 'cherry': 6}
# Note: The dictionary comprehension creates a dictionary with fruit names as keys and their lengths as values.
# This is useful for creating mappings or key-value pairs from existing data.
# You can also use list comprehensions with sets.
# Example:
fruits = ["apple", "banana", "cherry"]
fruits_set = {fruit for fruit in fruits}
print(fruits_set)  # Output: {'apple', 'banana', 'cherry'}
# Note: The set comprehension creates a set of unique fruit names from the list.
# This is useful for removing duplicates and creating a collection of unique items.
# Sets
# Sets are unordered collections of unique items.
# Sets are defined using curly braces {} or the set() constructor.
# Sets are mutable and do not allow duplicate items.
# Example:
fruits_set = {"apple", "banana", "cherry"}
print(fruits_set)  # Output: {'banana', 'cherry', 'apple'}
print(type(fruits_set))  # Output: <class 'set'>
print(len(fruits_set))  # Output: 3 (number of unique items)
print("apple" in fruits_set)  # Membership: True
print("grape" not in fruits_set)  # Membership: True
print(fruits_set.add("orange"))  # Add an item to the set
print(fruits_set)  # Output: {'banana', 'cherry', 'apple', 'orange'}

print(fruits_set.remove("banana"))  # Remove an item from the set
print(fruits_set)  # Output: {'cherry', 'apple', 'orange'}

print(fruits_set.discard("grape"))  # Discard an item (no error if not found)
print(fruits_set)  # Output: {'cherry', 'apple', 'orange'}

print(fruits_set.pop())  # Remove and return an arbitrary item from the set
print(fruits_set)  # Output: {'apple', 'orange'}
print(fruits_set.clear())  # Remove all items from the set
print(fruits_set)  # Output: set() (empty set)

print(fruits_set = set())  # Create an empty set
print(type(fruits_set))  # Output: <class 'set'>
print(len(fruits_set))  # Output: 0 (empty set)


print(fruits_set = set([1, 2, 3, 4]))  # Create a set from a list
print(fruits_set)  # Output: {1, 2, 3, 4}
print(type(fruits_set))  # Output: <class 'set'>


print(fruits_set = set("apple"))  # Create a set from a string
print(fruits_set)  # Output: {'a', 'p', 'l', 'e'}
print(type(fruits_set))  # Output: <class 'set'>


print(fruits_set = set((1, 2, 3)))  # Create a set from a tuple
print(fruits_set)  # Output: {1, 2, 3}




print(fruits_set = set({1, 2, 3}))  # Create a set from another set
print(fruits_set)  # Output: {1, 2, 3}


print(fruits_set = set({1, 2, 3, 3}))  # Create a set with duplicate items
print(fruits_set)  # Output: {1, 2, 3} (duplicates removed)





# Set Methods
# Sets have several built-in methods for manipulation.
# Example:
fruits_set = {"apple", "banana", "cherry"}
print(fruits_set)  # Output: {'banana', 'cherry', 'apple'}
print(fruits_set.add("orange"))  # Add an item to the set
print(fruits_set)  # Output: {'banana', 'cherry', 'apple', 'orange'}
print(fruits_set.remove("banana"))  # Remove an item from the set
print(fruits_set)  # Output: {'cherry', 'apple', 'orange'}
print(fruits_set.discard("grape"))  # Discard an item (no error if not found)
print(fruits_set)  # Output: {'cherry', 'apple', 'orange'}
print(fruits_set.pop())  # Remove and return an arbitrary item from the set
print(fruits_set)  # Output: {'apple', 'orange'}
print(fruits_set.clear())  # Remove all items from the set
print(fruits_set)  # Output: set() (empty set)
print(fruits_set = set())  # Create an empty set
print(type(fruits_set))  # Output: <class 'set'>
print(len(fruits_set))  # Output: 0 (empty set)
print(fruits_set = set([1, 2, 3, 4]))  # Create a set from a list
print(fruits_set)  # Output: {1, 2, 3, 4}
print(type(fruits_set))  # Output: <class 'set'>
print(fruits_set = set("apple"))  # Create a set from a string
print(fruits_set)  # Output: {'a', 'p', 'l', 'e'}


# Dictionaries
# Dictionaries are unordered collections of key-value pairs.
# Dictionaries are defined using curly braces {} or the dict() constructor.
# Dictionaries are mutable and allow duplicate keys.
# Example:
fruits_dict = {"apple": 1, "banana": 2, "cherry": 3}
print(fruits_dict)  # Output: {'apple': 1, 'banana': 2, 'cherry': 3}
print(type(fruits_dict))  # Output: <class 'dict'>
print(len(fruits_dict))  # Output: 3 (number of key-value pairs)


print(fruits_dict["apple"])  # Output: 1 (value associated with the key "apple")

print(fruits_dict.get("banana"))  # Output: 2 (value associated with the key "banana")
print(fruits_dict.keys())  # Output: dict_keys(['apple', 'banana', 'cherry']) (keys in the dictionary)
print(fruits_dict.values())  # Output: dict_values([1, 2, 3]) (values in the dictionary)
print(fruits_dict.items())  # Output: dict_items([('apple', 1), ('banana', 2), ('cherry', 3)]) (key-value pairs in the dictionary)
print("apple" in fruits_dict)  # Membership: True (key "apple" exists in the dictionary)
print("grape" not in fruits_dict)  # Membership: True (key "grape" does not exist in the dictionary)




# file read and write
# File handling is used to read and write files in Python.
# Python has built-in functions for file handling, such as open(), read(), write(), and close().
# Example:
# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a test file.")


# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)  # Output: Hello, World!\nThis is a test file.



# Reading line by line
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())  # Output: Hello, World! (line 1), This is a test file. (line 2)


# Reading specific lines
with open("example.txt", "r") as file:
    lines = file.readlines()
    print(lines[0].strip())  # Output: Hello, World! (line 1)
    print(lines[1].strip())  # Output: This is a test file. (line 2)

# Note: The open() function is used to open a file in a specific mode (read, write, append, etc.).
# The with statement is used to automatically close the file after the block of code is executed.
# The read() method reads the entire file content as a string.



# The readlines() method reads the file line by line and returns a list of lines.
# The strip() method is used to remove leading and trailing whitespace characters (including newlines) from each line.
# This is useful for cleaning up the output when printing lines from a file.
# The for loop iterates over each line in the file, allowing you to process each line individually. 
# This is useful for reading large files or processing data line by line.
# You can also use the read() method with a specific number of bytes to read a portion of the file.
# Example:
with open("example.txt", "r") as file:
    content = file.read(5)  # Read the first 5 bytes
    print(content)  # Output: Hello (first 5 bytes of the file)
# Note: The read() method can take an optional argument specifying the number of bytes to read. 
# If no argument is provided, it reads the entire file content.
# This is useful for reading large files or processing data in chunks.
# The read() method returns a string containing the read bytes.
# You can also use the readline() method to read a single line from the file.
# Example:
with open("example.txt", "r") as file:
    line = file.readline()  # Read the first line
    print(line.strip())  # Output: Hello, World! (line 1)
# Note: The readline() method reads a single line from the file and returns it as a string. 
# It includes the newline character at the end of the line.
# You can call readline() multiple times to read subsequent lines from the file.    
# This is useful for reading files line by line without loading the entire file into memory.
# The readline() method can also take an optional argument specifying the maximum number of bytes to read.
# Example:
with open("example.txt", "r") as file:
    line = file.readline(10)  # Read the first 10 bytes of the first line
    print(line.strip())  # Output: Hello, Wo (first 10 bytes of line 1)
# Note: The readline() method can take an optional argument specifying the maximum number of bytes to read.
# If no argument is provided, it reads the entire line until the newline character is encountered.
# This is useful for reading long lines or processing data in chunks.
# The readline() method returns a string containing the read bytes, including the newline character at the end of the line.
# You can also use the write() method to write data to a file.
# Example:
with open("example.txt", "a") as file:
    file.write("\nThis is an appended line.")
# Note: The write() method appends the specified string to the end of the file.
# If the file does not exist, it creates a new file.
# This is useful for adding data to existing files without overwriting the existing content.
# The write() method does not add a newline character automatically, so you need to include it if needed.
# Example:
with open("example.txt", "a") as file:
    file.write("\nThis is another appended line.")
# Note: The write() method appends the specified string to the end of the file.
# If the file does not exist, it creates a new file.


# working with binary files
# Binary files are files that contain data in binary format (not human-readable).
# Python provides built-in functions for reading and writing binary files.
# Example:
with open("example.bin", "wb") as file:
    file.write(b"Hello, World!")  # Write binary data to the file


with open("example.bin", "rb") as file:
    content = file.read()  # Read binary data from the file
    print(content)  # Output: b'Hello, World!' (binary data as bytes)
# Note: The "wb" mode is used to write binary data to the file, while the "rb" mode is used to read binary data from the file.
# The b prefix indicates that the string is in binary format (bytes).
# This is useful for working with non-text files, such as images, audio files, or other binary data.
# The read() method reads the entire file content as bytes.
# You can also use the read() method with a specific number of bytes to read a portion of the file.


# working with csv files
# CSV (Comma-Separated Values) files are used to store tabular data in plain text format.
# Python provides built-in functions for reading and writing CSV files.
# Example:
import csv

# Writing to a CSV file
with open("example.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Alice", 30, "New York"])
    writer.writerow(["Bob", 25, "Los Angeles"])


# Reading from a CSV file
with open("example.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # Output: ['Name', 'Age', 'City'], ['Alice', '30', 'New York'], ['Bob', '25', 'Los Angeles']
# Note: The csv module provides functions for reading and writing CSV files.
# The csv.writer() function creates a CSV writer object that can write data to a CSV file.
# The writerow() method writes a single row to the CSV file.
# The csv.reader() function creates a CSV reader object that can read data from a CSV file.
# The reader object can be iterated over to read each row of the CSV file.
# This is useful for processing tabular data in a structured format.
# The newline="" argument is used to prevent extra blank lines from being added when writing to the CSV file.
# This is important for maintaining the correct format of the CSV file.
# You can also use the csv.DictWriter() and csv.DictReader() classes to work with CSV files using dictionaries.
# Example:
import csv


# Writing to a CSV file using DictWriter
with open("example.csv", "w", newline="") as file:
    fieldnames = ["Name", "Age", "City"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"Name": "Alice", "Age": 30, "City": "New York"})
    writer.writerow({"Name": "Bob", "Age": 25, "City": "Los Angeles"})


# Reading from a CSV file using DictReader

with open("example.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)  # Output: {'Name': 'Alice', 'Age': '30', 'City': 'New York'}, {'Name': 'Bob', 'Age': '25', 'City': 'Los Angeles'}
# Note: The csv.DictWriter() class allows you to write data to a CSV file using dictionaries.
# The writeheader() method writes the header row to the CSV file.
# The writerow() method writes a single row to the CSV file using a dictionary.
# The csv.DictReader() class allows you to read data from a CSV file using dictionaries.
# The reader object can be iterated over to read each row of the CSV file as a dictionary.
# This is useful for processing tabular data in a structured format.
# The fieldnames argument specifies the order of the columns in the CSV file.
# This is important for maintaining the correct format of the CSV file.
# You can also use the csv module to handle different delimiters and quote characters in CSV files.
# Example:
import csv

# Writing to a CSV file with a custom delimiter
with open("example.csv", "w", newline="") as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Alice", 30, "New York"])
    writer.writerow(["Bob", 25, "Los Angeles"])
    

# Reading from a CSV file with a custom delimiter
with open("example.csv", "r") as file:
    reader = csv.reader(file, delimiter=";")
    for row in reader:
        print(row)  # Output: ['Name', 'Age', 'City'], ['Alice', '30', 'New York'], ['Bob', '25', 'Los Angeles']
# Note: The delimiter argument specifies the character used to separate values in the CSV file.
# The default delimiter is a comma (,), but you can specify any character as the delimiter.
# This is useful for working with CSV files that use different delimiters.

# The csv module also provides functions for handling different quote characters in CSV files.
# Example:
import csv


# Writing to a CSV file with custom quote character
with open("example.csv", "w", newline="") as file:
    writer = csv.writer(file, quotechar="'")
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Alice", 30, "New York"])
    writer.writerow(["Bob", 25, "Los Angeles"])


# Reading from a CSV file with custom quote character
with open("example.csv", "r") as file:
    reader = csv.reader(file, quotechar="'")
    for row in reader:
        print(row)  # Output: ['Name', 'Age', 'City'], ['Alice', '30', 'New York'], ['Bob', '25', 'Los Angeles']

# Note: The quotechar argument specifies the character used to quote fields in the CSV file.
# The default quote character is a double quote ("), but you can specify any character as the quote character.
# This is useful for working with CSV files that use different quote characters.
# The csv module also provides functions for handling different escape characters in CSV files.



# Connecting to a Database
# Python provides built-in modules for connecting to databases, such as SQLite and MySQL.

# MySQL Database Connection Example
import mysql.connector

# Establish a connection to the MySQL database

connection = mysql.connector.connect()
# Replace with your database credentials

# Create a cursor object to execute SQL queries
cursor = connection.cursor()
# Execute a SQL query
cursor.execute("SELECT * FROM users")
# Fetch all rows from the result set

# Fetch the column names using the cursor's description
columns = [description[0] for description in cursor.description]

rows = cursor.fetchall()
# Print the rows
for row in rows:
    print(row)
# Close the cursor and connection
cursor.close()
connection.close()
# Note: The mysql.connector module is used to connect to MySQL databases.
# The connect() function establishes a connection to the MySQL database using the provided credentials.
# The cursor() method creates a cursor object that can execute SQL queries.

# Adding to the database

import sqlite3

# Connect to SQLite database (it will create the file if it doesn't exist)
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create a table (if it doesn't already exist)
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER
)
''')

# Insert data into the 'users' table
cursor.execute('''
INSERT INTO users (name, age)
VALUES (?, ?)
''', ('Alice', 25))

# Commit the transaction
conn.commit()

# Insert another record
cursor.execute('''
INSERT INTO users (name, age)
VALUES (?, ?)
''', ('Bob', 30))

# Commit the second transaction
conn.commit()

# Fetch all records to see the inserted data
cursor.execute('SELECT * FROM users')
print(cursor.fetchall())  # Print all records in the 'users' table

# Close the cursor and connection
cursor.close()
conn.close()
# Note: The sqlite3 module is used to connect to SQLite databases.



# Connecting to the internet
# Python provides built-in modules for connecting to the internet, such as urllib and requests.
# The requests module is a popular third-party library for making HTTP requests.
# Example:
import requests



# Sending a GET request to a URL
response = requests.get("https://api.github.com")
print(response.status_code)  # Output: 200 (OK)
print(response.json())  # Output: JSON response from the API
# Note: The requests module is used to send HTTP requests to web servers.
# The get() function sends a GET request to the specified URL and returns the response.
# The status_code attribute contains the HTTP status code of the response.
# The json() method parses the response content as JSON and returns it as a Python dictionary.
# This is useful for working with RESTful APIs and retrieving data from web services.
# The requests module also provides functions for sending POST, PUT, DELETE, and other types of HTTP requests.
# Example:
import requests



# Sending a POST request to a URL
response = requests.post("https://api.github.com", data={"key": "value"})
print(response.status_code)  # Output: 200 (OK)
print(response.json())  # Output: JSON response from the API
# Note: The post() function sends a POST request to the specified URL with the provided data.
# The data argument can be a dictionary, string, or file-like object.
# The requests module also provides functions for sending custom headers, authentication, and handling cookies.
# Example:
import requests


# Sending a GET request with custom headers
response = requests.get("https://api.github.com", headers={"User-Agent": "MyApp"})
print(response.status_code)  # Output: 200 (OK)
print(response.json())  # Output: JSON response from the API
# Note: The headers argument allows you to specify custom HTTP headers for the request.
# This is useful for setting user-agent strings, authentication tokens, and other custom headers.
# The requests module also provides functions for handling query parameters and URL encoding.

#authentication
import requests
from requests.auth import HTTPBasicAuth


# Sending a GET request with basic authentication
response = requests.get("https://api.github.com/user", auth=HTTPBasicAuth("username", "password"))
print(response.status_code)  # Output: 200 (OK)
print(response.json())  # Output: JSON response from the API
# Note: The HTTPBasicAuth class is used to create basic authentication credentials.
# The auth argument allows you to specify the username and password for basic authentication.
# This is useful for accessing protected resources that require authentication.
# The requests module also provides functions for handling OAuth and other authentication methods.
# Example:
import requests

from requests_oauthlib import OAuth1
from requests_oauthlib import OAuth2Session

from requests.auth import HTTPBasicAuth

# Sending a GET request with OAuth1 authentication

import requests
from requests_oauthlib import OAuth1

# OAuth1 credentials (replace these with your actual credentials)
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

# Create an OAuth1 object with the credentials
auth = OAuth1(consumer_key, consumer_secret, access_token, access_token_secret)

# Define the API endpoint (Twitter example)
url = 'https://api.twitter.com/1.1/account/verify_credentials.json'

# Send the GET request with OAuth1 authentication
response = requests.get(url, auth=auth)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    print("Request successful!")
    print(response.json())  # Print the JSON response
else:
    print(f"Request failed with status code: {response.status_code}")
    print(response.text)


## scraping# Web scraping is the process of extracting data from websites.
# Python provides libraries like BeautifulSoup and Scrapy for web scraping.
# BeautifulSoup is a popular library for parsing HTML and XML documents.

