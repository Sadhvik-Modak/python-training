# Session 3: Control Flow

## Overview

In this session, we will explore the control flow mechanisms in Python. Control flow statements allow you to dictate the order in which instructions are executed in your program. We will cover conditional statements (`if`, `elif`, `else`), loops (`for`, `while`), and an introduction to error handling using the `try` and `except` statements.

## Topics Covered

1. Conditional Statements
2. Loops
3. Introduction to Error Handling

## 1. Conditional Statements

Conditional statements allow you to execute specific blocks of code based on certain conditions. Python supports `if`, `elif`, and `else` statements.

### Syntax

```python
if condition:
    # Code to execute if condition is true
elif another_condition:
    # Code to execute if another_condition is true
else:
    # Code to execute if all conditions are false
```

### Examples

#### Basic `if` Statement

```python
x = 10

if x > 5:
    print("x is greater than 5")
```

#### `if-else` Statement

```python
x = 10

if x > 15:
    print("x is greater than 15")
else:
    print("x is not greater than 15")
```

#### `if-elif-else` Statement

```python
x = 10

if x > 15:
    print("x is greater than 15")
elif x == 10:
    print("x is equal to 10")
else:
    print("x is less than 10")
```

### Nested Conditional Statements

You can nest `if` statements inside other `if` statements to create more complex conditions.

```python
x = 10
y = 20

if x > 5:
    if y > 15:
        print("x is greater than 5 and y is greater than 15")
    else:
        print("x is greater than 5 but y is not greater than 15")
```

## 2. Loops

Loops allow you to execute a block of code multiple times. Python supports `for` and `while` loops.

### `for` Loop

The `for` loop is used to iterate over a sequence (such as a list, tuple, string, or range).

#### Syntax

```python
for item in sequence:
    # Code to execute for each item in sequence
```

#### Examples

##### Iterating Over a List

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

##### Using `range()`

```python
for i in range(5):
    print(i)
```

### `while` Loop

The `while` loop is used to execute a block of code as long as a condition is true.

#### Syntax

```python
while condition:
    # Code to execute while condition is true
```

#### Examples

##### Basic `while` Loop

```python
i = 0

while i < 5:
    print(i)
    i += 1
```

### `break` and `continue` Statements

- `break`: Exits the loop immediately.
- `continue`: Skips the rest of the current iteration and moves to the next iteration.

#### Examples

##### Using `break`

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

##### Using `continue`

```python
for i in range(10):
    if i == 5:
        continue
    print(i)
```

Certainly! Here is the expanded section on error handling with more detailed examples.

## 3. Introduction to Error Handling

Error handling allows you to manage errors that occur during the execution of your program. Python uses the `try`, `except`, `else`, and `finally` statements to handle exceptions.

### Syntax

```python
try:
    # Code that might raise an exception
except SomeException as e:
    # Code to execute if an exception occurs
else:
    # Code to execute if no exception occurs
finally:
    # Code to execute regardless of whether an exception occurs
```

### Examples

#### Basic `try-except`

```python
try:
    x = 1 / 0
except ZeroDivisionError as e:
    print("Error: Cannot divide by zero")
```

#### Handling Multiple Exceptions

```python
try:
    x = int("not a number")
except ValueError as e:
    print("Error: Invalid value")
except ZeroDivisionError as e:
    print("Error: Cannot divide by zero")
```

#### Using `else` and `finally`

```python
try:
    x = 1 / 1
except ZeroDivisionError as e:
    print("Error: Cannot divide by zero")
else:
    print("No error occurred")
finally:
    print("This block is always executed")
```

#### Raising Exceptions

You can raise exceptions using the `raise` keyword.

##### Example

```python
def check_positive(number):
    if number < 0:
        raise ValueError("Number must be positive")

try:
    check_positive(-1)
except ValueError as e:
    print(e)
```

### More Error Handling Examples

#### Catching Any Exception

You can catch any exception using a bare `except` clause. However, it's generally better to catch specific exceptions.

```python
try:
    x = 1 / 0
except:
    print("An error occurred")
```

#### Logging Exceptions

It's often useful to log exceptions for debugging purposes. The `logging` module provides a flexible framework for logging messages in your applications.

```python
import logging

logging.basicConfig(level=logging.ERROR)

try:
    x = 1 / 0
except ZeroDivisionError as e:
    logging.error("Error: Cannot divide by zero", exc_info=True)
```

#### Custom Exception Classes

You can define your own exception classes by inheriting from the built-in `Exception` class.

```python
class CustomError(Exception):
    """Custom exception class"""
    pass

def do_something():
    raise CustomError("This is a custom error")

try:
    do_something()
except CustomError as e:
    print(f"Caught custom error: {e}")
```

#### Using `finally` for Cleanup

The `finally` block is useful for cleaning up resources, such as closing files or releasing locks, regardless of whether an exception occurred.

```python
try:
    file = open("example.txt", "r")
    # Perform file operations
finally:
    file.close()
```

#### Nested `try-except` Blocks

You can nest `try-except` blocks to handle different exceptions at different levels.

```python
try:
    try:
        x = 1 / 0
    except ZeroDivisionError as e:
        print("Inner error: Cannot divide by zero")
        raise
except Exception as e:
    print(f"Outer error: {e}")
```

#### Using Assertions

Assertions are a debugging aid that tests a condition as an internal self-check in your program. If the condition is `False`, an `AssertionError` is raised.

```python
def divide(a, b):
    assert b != 0, "Division by zero is not allowed"
    return a / b

try:
    divide(10, 0)
except AssertionError as e:
    print(f"Assertion error: {e}")
```

### Summary of Best Practices

1. **Catch Specific Exceptions**: Catch specific exceptions rather than using a bare `except` clause.
2. **Use `finally` for Cleanup**: Ensure resources are cleaned up using the `finally` block.
3. **Log Exceptions**: Use the `logging` module to log exceptions for debugging purposes.
4. **Avoid Silent Failures**: Do not use empty `except` clauses. Always handle exceptions appropriately.
5. **Create Custom Exceptions**: Define custom exception classes for specific error conditions in your application.
6. **Document Exception Handling**: Use docstrings to document what exceptions a function might raise and how they are handled.
