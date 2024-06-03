Sure! Let's prepare a comprehensive session on Encapsulation, including both theoretical aspects and practical code examples.

## KT Session: Encapsulation in Python

### Introduction to Encapsulation (Theory)

**Definition**:
Encapsulation is one of the fundamental principles of Object-Oriented Programming (OOP). It refers to the bundling of data (attributes) and methods (functions) that operate on the data into a single unit or class. Encapsulation also involves restricting direct access to some of an object's components, which can prevent the accidental modification of data.

**Key Concepts**:
1. **Private Attributes and Methods**: Encapsulation allows for the definition of private attributes and methods, which are not accessible directly from outside the class. These are intended to be used only within the class.
2. **Public Attributes and Methods**: Public attributes and methods can be accessed from outside the class.
3. **Getter and Setter Methods**: These are public methods that allow indirect access to private attributes. They are used to get and set the values of private attributes in a controlled way.

**Benefits of Encapsulation**:
- **Data Hiding**: Encapsulation helps to hide the internal state of an object and only expose a controlled interface to the outside world.
- **Modularity**: It allows for modular code, where the internal workings of a class can be changed without affecting other parts of the program.
- **Ease of Maintenance**: Encapsulation helps in maintaining and updating code easily because changes to the class's internal implementation do not affect its external interface.
- **Increased Security**: By controlling access to data, encapsulation can protect the integrity of an object's state.

### Practical Examples of Encapsulation

#### Example 1: Basic Encapsulation

This example demonstrates how to define a class with private attributes and how to use getter and setter methods to access and modify those attributes.

```python
class Student:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self.__age = age    # Private attribute

    # Getter method for name
    def get_name(self):
        return self.__name

    # Setter method for name
    def set_name(self, name):
        self.__name = name

    # Getter method for age
    def get_age(self):
        return self.__age

    # Setter method for age
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive")

# Create an object of the Student class
student = Student("Alice", 20)

# Accessing private attributes using getter methods
print(student.get_name())  # Output: Alice
print(student.get_age())   # Output: 20

# Modifying private attributes using setter methods
student.set_name("Bob")
student.set_age(25)
print(student.get_name())  # Output: Bob
print(student.get_age())   # Output: 25

# Attempting to set an invalid age
student.set_age(-5)        # Output: Age must be positive
print(student.get_age())   # Output: 25
```

#### Example 2: Encapsulation with Public Methods

This example shows how encapsulation works with public methods to control access to private attributes.

```python
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Private attribute
        self.__balance = balance                # Private attribute

    # Public method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive")

    # Public method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdrawal amount")

    # Public method to get the current balance
    def get_balance(self):
        return self.__balance

# Create an object of the BankAccount class
account = BankAccount("123456789", 1000)

# Deposit money into the account
account.deposit(500)
print(account.get_balance())  # Output: 1500

# Withdraw money from the account
account.withdraw(200)
print(account.get_balance())  # Output: 1300

# Attempting to withdraw an invalid amount
account.withdraw(2000)        # Output: Invalid withdrawal amount
print(account.get_balance())  # Output: 1300
```

#### Example 3: Encapsulation with Inheritance

This example demonstrates encapsulation in a class hierarchy where a derived class inherits from a base class and accesses private attributes through public methods.

```python
class Person:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self.__age = age    # Private attribute

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive")

class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.__employee_id = employee_id  # Private attribute

    def get_employee_id(self):
        return self.__employee_id

# Create an object of the Employee class
employee = Employee("Charlie", 30, "E123")

# Access inherited private attributes using public methods
print(employee.get_name())       # Output: Charlie
print(employee.get_age())        # Output: 30

# Modify inherited private attributes using public methods
employee.set_age(35)
print(employee.get_age())        # Output: 35

# Access private attribute of derived class using public method
print(employee.get_employee_id())  # Output: E123
```

### Summary

- **Encapsulation**: The bundling of data and methods that operate on the data within a single unit or class. It restricts direct access to some of an object's components.
- **Private Attributes and Methods**: Encapsulation allows defining private attributes and methods that are not accessible directly from outside the class.
- **Public Attributes and Methods**: Public attributes and methods can be accessed from outside the class.
- **Getter and Setter Methods**: Public methods that provide controlled access to private attributes.
- **Benefits**: Data hiding, modularity, ease of maintenance, and increased security.

### Q&A (5 minutes)

- Open the floor for any questions from the interns to clarify their understanding of encapsulation.

### Next Steps

- Encourage interns to practice by creating their own classes with encapsulation.
- Suggest reading further materials or tutorials on OOP principles in Python.

By the end of this session, interns should have a solid understanding of encapsulation, its benefits, and how to implement it in Python. This foundation will help them write more secure, maintainable, and modular code.