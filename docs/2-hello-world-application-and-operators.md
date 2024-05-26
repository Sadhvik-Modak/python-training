# Session 2: Hello World Application

## Overview

In this session, we will write and run our first Python program. We will also learn about basic input and output operations, get an introduction to functions in Python, and understand various operators used in Python programming.

## Topics Covered

1. Basic Input and Output
2. Introduction to Functions
3. Operators in Python

## 1. Basic Input and Output

### Output

Python uses the `print()` function to output data to the standard output.

#### Examples

```python
# Print a string
print("Hello, World!")

# Print multiple items
print("Hello,", "World!")

# Print numbers
print(123, 456.789)

# Print with a separator
print("Hello", "World", sep="-")
```

#### Output Formatting

You can format the output using formatted string literals (f-strings), the `str.format()` method, or the `%` operator.

```python
name = "Alice"
age = 25

# Using f-strings (Python 3.6+)
print(f"Name: {name}, Age: {age}")

# Using str.format()
print("Name: {}, Age: {}".format(name, age))

# Using % operator
print("Name: %s, Age: %d" % (name, age))
```

### Input

Python uses the `input()` function to read data from the standard input (usually the keyboard).

#### Examples

```python
# Read a string input
name = input("Enter your name: ")
print(f"Hello, {name}!")

# Read a number input and convert it to an integer
age = int(input("Enter your age: "))
print(f"Age: {age}")
```

#### Internal Working

- The `input()` function displays a prompt and waits for the user to enter data. It reads the input as a string.
- The `print()` function outputs data to the standard output.

## 2. Introduction to Functions

Functions are reusable blocks of code that perform a specific task. Functions help in organizing code, making it more modular, and improving readability and reusability.

### Defining Functions

You can define a function using the `def` keyword followed by the function name and parentheses `()`.

#### Syntax

```python
def function_name(parameters):
    """Docstring describing the function."""
    # Function body
    return value
```

### Examples

#### Simple Function

```python
# Define a function that prints a greeting
def greet():
    print("Hello, World!")

# Call the function
greet()
```

#### Function with Parameters

```python
# Define a function that takes a name as a parameter and prints a greeting
def greet(name):
    print(f"Hello, {name}!")

# Call the function with an argument
greet("Alice")
```

#### Function with Return Value

```python
# Define a function that takes two numbers and returns their sum
def add(a, b):
    return a + b

# Call the function and store the result in a variable
result = add(5, 3)
print(f"The sum is: {result}")
```

### Function Scope and Lifetime

- **Scope**: The scope of a variable refers to the region of the code where the variable is accessible. Variables defined inside a function are local to that function.
- **Lifetime**: The lifetime of a variable is the period during which the variable exists in memory. Local variables exist only during the execution of the function.

#### Example of Variable Scope

```python
def my_function():
    local_variable = 10  # Local variable
    print(local_variable)

my_function()
# print(local_variable)  # This will cause an error because local_variable is not accessible outside the function
```

### Docstrings

Docstrings are used to describe the purpose of a function. They are written as the first statement in the function and are enclosed in triple quotes.

#### Example with Docstring

```python
def add(a, b):
    """
    Calculate the sum of two numbers.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The sum of the two numbers.
    """
    return a + b
```

### Best Practices for Functions

1. **Use Descriptive Names**: Function names should clearly describe the purpose of the function.
2. **Keep Functions Small**: Each function should perform a single task.
3. **Use Docstrings**: Document the purpose, parameters, and return values of functions.
4. **Avoid Global Variables**: Prefer passing parameters to functions and returning results.

## 3. Operators in Python

Operators are special symbols in Python that perform operations on variables and values. Python supports various types of operators, including arithmetic, comparison, logical, assignment, bitwise, and more.

### Arithmetic Operators

Arithmetic operators are used to perform mathematical operations.

| Operator | Description       | Example       |
|----------|-------------------|---------------|
| `+`      | Addition          | `a + b`       |
| `-`      | Subtraction       | `a - b`       |
| `*`      | Multiplication    | `a * b`       |
| `/`      | Division          | `a / b`       |
| `%`      | Modulus           | `a % b`       |
| `**`     | Exponentiation    | `a ** b`      |
| `//`     | Floor Division    | `a // b`      |

#### Examples

```python
a = 10
b = 3

print(a + b)   # Output: 13
print(a - b)   # Output: 7
print(a * b)   # Output: 30
print(a / b)   # Output: 3.3333333333333335
print(a % b)   # Output: 1
print(a ** b)  # Output: 1000
print(a // b)  # Output: 3
```

### Comparison Operators

Comparison operators are used to compare two values.

| Operator | Description                  | Example       |
|----------|------------------------------|---------------|
| `==`     | Equal to                     | `a == b`      |
| `!=`     | Not equal to                 | `a != b`      |
| `>`      | Greater than                 | `a > b`       |
| `<`      | Less than                    | `a < b`       |
| `>=`     | Greater than or equal to     | `a >= b`      |
| `<=`     | Less than or equal to        | `a <= b`      |

#### Examples

```python
a = 10
b = 3

print(a == b)  # Output: False
print(a != b)  # Output: True
print(a > b)   # Output: True
print(a < b)   # Output: False
print(a >= b)  # Output: True
print(a <= b)  # Output: False
```

### Logical Operators

Logical operators are used to combine conditional statements.

| Operator | Description                  | Example              |
|----------|------------------------------|----------------------|
| `and`    | Returns True if both statements are true | `a and b` |
| `or`     | Returns True if one of the statements is true | `a or b` |
| `not`    | Reverses the result, returns False if the result is true | `not a` |

#### Examples

```python
a = True
b = False

print(a and b)  # Output: False
print(a or b)   # Output: True
print(not a)    # Output: False
```

### Assignment Operators

Assignment operators are used to assign values to variables.

| Operator | Description                  | Example       |
|----------|------------------------------|---------------|
| `=`      | Assign                       | `a = b`       |
| `+=`     | Add and assign               | `a += b`      |
| `-=`     | Subtract and assign          | `a -= b`      |
| `*=`     | Multiply and assign          | `a *= b`      |
| `/=`     | Divide and assign            | `a /= b`      |
| `%=`     | Modulus and assign           | `a %= b`      |
| `**=`    | Exponentiation and assign    | `a **= b`     |
| `//=`    | Floor division and assign    | `a //= b`     |

#### Examples

```python
a = 10
b = 3

a += b  # Equivalent to a = a + b
print(a)  # Output: 13

a -= b  # Equivalent to a = a - b
print(a)  # Output: 10

a *= b  # Equivalent to a = a * b
print(a)  # Output: 30

a /= b  # Equivalent to a = a / b
print(a)  # Output: 10.0

a %= b  # Equivalent to a = a % b
print(a)  # Output: 1.0

a **= b  # Equivalent to a = a ** b
print(a)  # Output: 1.0

a //= b  # Equivalent to a = a // b
print(a)  # Output: 0.0
```

### Bitwise Operators

Bitwise operators are used to perform bit-level operations.

| Operator | Description                  | Example       |
|----------|------------------------------|---------------|
| `&`      | AND                          | `a & b`       |
| `|`      | OR                           | `a | b`       |
| `^`      | XOR                          | `a ^ b`       |
| `~`      | NOT                          | `~a`          |
| `<<`     | Left shift                   | `a << b`      |
| `>>`     | Right shift                  | `a >> b`      |

#### Examples

```python
a = 10  # Binary: 1010
b = 3   # Binary: 0011

print(a & b)  # Output: 2  (Binary: 0010)
print(a | b)  # Output: 11 (Binary: 1011)
print(a ^ b)  # Output: 9  (Binary: 1001)
print(~a)     # Output: -11 (Binary: ...11110101 in two's complement)
print(a << 2) # Output: 40 (Binary: 101000)
print(a >> 2) # Output: 2  (Binary: 0010)
```

### Membership Operators

Membership operators are used to test if a sequence contains an element.

| Operator | Description                  | Example       |
|----------|------------------------------|---------------|
| `in`     | Returns True if a sequence contains a specified element | `x in y` |
| `not in` | Returns True if a sequence does not contain a specified element | `x not in y` |

#### Examples

```python
a = [1, 2, 3, 4, 5]

print(3 in a)     # Output: True
print(6 in a)     # Output: False
print(3 not in a) # Output: False
print(6 not in a) # Output: True
```

### Identity Operators

Identity operators are used to compare the memory locations of two objects.

| Operator | Description                  | Example       |
|----------|------------------------------|---------------|
| `is`     | Returns True if both variables point to the same object | `x is y` |
| `is not` | Returns True if both variables do not point to the same object | `x is not y` |

#### Examples

```python
a = [1, 2, 3]
b = a
c = a[:]

print(a is b)      # Output: True (b is a reference to a)
print(a is c)      # Output: False (c is a copy of a)
print(a == c)      # Output: True (a and c have the same content)
print(a is not c)  # Output: True (a and c are not the same object)
```

### Operator Precedence

Operator precedence determines the order in which operations are performed. Operators with higher precedence are evaluated before operators with lower precedence.

| Operator         | Description                              |
|------------------|------------------------------------------|
| `**`             | Exponentiation                           |
| `~ + -`          | Complement, unary plus and minus (method names for the last two are `+@` and `-@`) |
| `* / % //`       | Multiplication, division, remainder, floor division |
| `+ -`            | Addition and subtraction                 |
| `>> <<`          | Right and left bitwise shift             |
| `&`              | Bitwise AND                              |
| `^ \|`           | Bitwise XOR and OR                       |
| `<= < > >=`      | Comparison operators                     |
| `<> == !=`       | Equality operators                       |
| `= %= /= //= -= += *= **=` | Assignment operators           |
| `is is not`      | Identity operators                       |
| `in not in`      | Membership operators                     |
| `not or and`     | Logical operators                        |

#### Example of Operator Precedence

```python
a = 3 + 4 * 2
# Multiplication has higher precedence than addition
# Equivalent to a = 3 + (4 * 2)
print(a)  # Output: 11

b = (3 + 4) * 2
# Parentheses alter the precedence
print(b)  # Output: 14
```