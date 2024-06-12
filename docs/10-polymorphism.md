### KT Session: Method Overloading and Method Overriding in Python

### Introduction to Method Overloading and Overriding

#### Method Overloading

**Definition**:
Method overloading refers to the ability to define multiple methods with the same name but different signatures (i.e., different parameters) within the same class. However, Python does not support method overloading in the same way that languages like Java or C++ do. Instead, Python allows method overloading by using default arguments or variable-length arguments.

**Example**:
Using default arguments to achieve method overloading.

```python
class Calculator:
    def add(self, a, b, c=0):
        return a + b + c

# Create an object of the Calculator class
calc = Calculator()

# Call the add method with different numbers of arguments
print(calc.add(1, 2))       # Output: 3
print(calc.add(1, 2, 3))    # Output: 6
```

Using variable-length arguments to achieve method overloading.

```python
class Calculator:
    def add(self, *args):
        return sum(args)

# Create an object of the Calculator class
calc = Calculator()

# Call the add method with different numbers of arguments
print(calc.add(1, 2))          # Output: 3
print(calc.add(1, 2, 3, 4))    # Output: 10
```

#### Method Overriding

**Definition**:
Method overriding occurs when a derived class provides a specific implementation of a method that is already defined in its base class. This allows the derived class to customize or extend the behavior of the base class method.

**Example**:
Basic method overriding in a derived class.

```python
class Animal:
    def speak(self):
        return "Some generic sound"

class Dog(Animal):
    def speak(self):
        return "Woof Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

# Create objects of the derived classes
dog = Dog()
cat = Cat()

# Call the overridden speak method
print(dog.speak())  # Output: Woof Woof
print(cat.speak())  # Output: Meow
```

Using the `super()` function to extend the behavior of the base class method.

```python
class Animal:
    def speak(self):
        return "Some generic sound"

class Dog(Animal):
    def speak(self):
        base_sound = super().speak()  # Call the method from the base class
        return f"{base_sound} and Woof Woof"

# Create an object of the Dog class
dog = Dog()

# Call the speak method
print(dog.speak())  # Output: Some generic sound and Woof Woof
```

### Summary

- **Method Overloading**: Python does not support traditional method overloading, but similar behavior can be achieved using default arguments or variable-length arguments.
- **Method Overriding**: Allows a derived class to provide a specific implementation of a method that is already defined in the base class.
