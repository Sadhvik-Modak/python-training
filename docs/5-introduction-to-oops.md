## KT Session: Introduction to OOP in Python

### Detailed Theory: Classes, Objects, and Constructors

#### 1. Classes

**Definition**:
A class is a blueprint for creating objects (a particular data structure), providing initial values for state (member variables or attributes), and implementations of behavior (member functions or methods).

**Components of a Class**:
- **Attributes**: Variables that belong to the class and define the state of its objects.
- **Methods**: Functions that belong to the class and define the behaviors of its objects.
- **Constructor**: A special method that initializes objects of the class.

**Syntax**:
```python
class ClassName:
    # Class attribute
    class_attribute = "value"

    # Constructor (initializer)
    def __init__(self, param1, param2):
        self.instance_attribute1 = param1
        self.instance_attribute2 = param2

    # Instance method
    def method_name(self):
        # Method body
        pass
```

#### 2. Objects

**Definition**:
An object is an instance of a class. When a class is defined, no memory is allocated until an object of that class is created.

**Creating an Object**:
To create an object, you call the class using the class name and pass any arguments that the constructor requires.
```python
object_name = ClassName(arg1, arg2)
```

#### 3. Constructors

**Definition**:
A constructor is a special method in Python that is automatically called when an object is created. The constructor is used to initialize the object's attributes.

**Types of Constructors**:
- **Default Constructor**: Does not accept any arguments other than `self`.
- **Parameterized Constructor**: Accepts arguments to initialize the object's attributes.

**Syntax**:
```python
class ClassName:
    def __init__(self, param1, param2):
        self.attribute1 = param1
        self.attribute2 = param2
```

### Practical Code Examples

#### Example 1: Basic Class and Object

```python
# Define a class
class Dog:
    # Class attribute
    species = "Canis familiaris"

    # Constructor (initializer)
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

# Create an object of the Dog class
my_dog = Dog("Buddy", 3)

# Access class attribute
print(my_dog.species)  # Output: Canis familiaris

# Access instance attributes
print(my_dog.name)  # Output: Buddy
print(my_dog.age)   # Output: 3

# Call instance methods
print(my_dog.description())  # Output: Buddy is 3 years old
print(my_dog.speak("Woof Woof"))  # Output: Buddy says Woof Woof
```

#### Example 2: Using a Parameterized Constructor

```python
# Define a class
class Car:
    # Constructor (initializer)
    def __init__(self, make, model, year):
        self.make = make    # Instance attribute
        self.model = model  # Instance attribute
        self.year = year    # Instance attribute

    # Instance method
    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

# Create objects of the Car class
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Honda", "Civic", 2018)

# Call instance methods
print(car1.display_info())  # Output: 2020 Toyota Corolla
print(car2.display_info())  # Output: 2018 Honda Civic
```

#### Example 3: Encapsulation with Private Attributes

```python
# Define a class
class Employee:
    # Constructor (initializer)
    def __init__(self, name, salary):
        self.name = name         # Public attribute
        self.__salary = salary   # Private attribute

    # Public method
    def display_employee(self):
        return f"Employee Name: {self.name}, Salary: {self.__salary}"

    # Public method to set salary
    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Invalid salary")

# Create an object of the Employee class
emp = Employee("John Doe", 50000)

# Access public attribute
print(emp.name)  # Output: John Doe

# Access private attribute (will raise an AttributeError)
# print(emp.__salary)  # Uncommenting this line will raise an error

# Use public method to access private attribute
print(emp.display_employee())  # Output: Employee Name: John Doe, Salary: 50000

# Use public method to modify private attribute
emp.set_salary(60000)
print(emp.display_employee())  # Output: Employee Name: John Doe, Salary: 60000
```

#### Example 4: Inheritance

```python
# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Derived class
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof Woof"

# Another derived class
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow"

# Create objects of the derived classes
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Call the speak method
print(dog.speak())  # Output: Buddy says Woof Woof
print(cat.speak())  # Output: Whiskers says Meow
```

### Summary

- **Classes**: Define the structure and behavior of objects.
- **Objects**: Instances of classes that hold data and can perform operations defined by methods.
- **Constructors**: Special methods to initialize objects.
- **Encapsulation**: Restricts access to certain components and protects object integrity.
- **Inheritance**: Allows one class to inherit attributes and methods from another class.

### Q&A (5 minutes)

- Open the floor for any questions from the interns to clarify their understanding of the concepts discussed.

### Next Steps

- Encourage interns to practice by creating their own classes and objects.
- Suggest reading further materials or tutorials on OOP in Python.

By the end of this session, interns should have a solid theoretical understanding of OOP concepts and some practical experience with creating and using classes and objects in Python. This foundation will prepare them for more advanced topics in OOP and software development.