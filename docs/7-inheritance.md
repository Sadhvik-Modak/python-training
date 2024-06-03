### KT Session: Inheritance in Python

#### 1. What is Inheritance?

**Definition**:
Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a class (known as the child or derived class) to inherit attributes and methods from another class (known as the parent or base class). This promotes code reuse and helps in creating a hierarchical relationship between classes.

**Key Benefits**:
- **Code Reusability**: Inherit code from existing classes to avoid duplication.
- **Modularity**: Organize code into logical hierarchies.
- **Maintainability**: Easier to manage and update code by modifying a single class.

#### 2. Types of Inheritance

1. **Single Inheritance**: A class inherits from one base class.
2. **Multiple Inheritance**: A class inherits from more than one base class.
3. **Multilevel Inheritance**: A class inherits from a base class, and another class inherits from that derived class.
4. **Hierarchical Inheritance**: Multiple classes inherit from a single base class.
5. **Hybrid Inheritance**: A combination of two or more types of inheritance.

#### 3. Each Inheritance Type with Examples

**Single Inheritance**:
One class inherits from one base class.

```python
class Animal:
    def speak(self):
        return "Animal sound"

class Dog(Animal):
    def bark(self):
        return "Woof Woof"

# Create an object of the Dog class
dog = Dog()
print(dog.speak())  # Output: Animal sound
print(dog.bark())   # Output: Woof Woof
```

**Multiple Inheritance**:
A class inherits from more than one base class.

```python
class A:
    def method_a(self):
        return "Method A"

class B:
    def method_b(self):
        return "Method B"

class C(A, B):
    def method_c(self):
        return "Method C"

# Create an object of the C class
c = C()
print(c.method_a())  # Output: Method A
print(c.method_b())  # Output: Method B
print(c.method_c())  # Output: Method C
```

**Multilevel Inheritance**:
A class inherits from another derived class.

```python
class Animal:
    def speak(self):
        return "Animal sound"

class Dog(Animal):
    def bark(self):
        return "Woof Woof"

class Puppy(Dog):
    def weep(self):
        return "Whimper"

# Create an object of the Puppy class
puppy = Puppy()
print(puppy.speak())  # Output: Animal sound
print(puppy.bark())   # Output: Woof Woof
print(puppy.weep())   # Output: Whimper
```

**Hierarchical Inheritance**:
Multiple classes inherit from a single base class.

```python
class Animal:
    def speak(self):
        return "Animal sound"

class Dog(Animal):
    def bark(self):
        return "Woof Woof"

class Cat(Animal):
    def meow(self):
        return "Meow"

# Create objects of the Dog and Cat classes
dog = Dog()
cat = Cat()
print(dog.speak())  # Output: Animal sound
print(dog.bark())   # Output: Woof Woof
print(cat.speak())  # Output: Animal sound
print(cat.meow())   # Output: Meow
```

**Hybrid Inheritance**:
A combination of two or more types of inheritance.

```python
class A:
    def method_a(self):
        return "Method A"

class B(A):
    def method_b(self):
        return "Method B"

class C(A):
    def method_c(self):
        return "Method C"

class D(B, C):
    def method_d(self):
        return "Method D"

# Create an object of the D class
d = D()
print(d.method_a())  # Output: Method A
print(d.method_b())  # Output: Method B
print(d.method_c())  # Output: Method C
print(d.method_d())  # Output: Method D
```

#### 4. Use of `self` and `super`

**`self`**:
- `self` is a reference to the current instance of the class.
- It is used to access attributes and methods of the class.
- Every instance method in a class should have `self` as its first parameter.

**Example**:
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}"

# Create an object of the Person class
person = Person("Alice", 30)
print(person.get_details())  # Output: Name: Alice, Age: 30
```

**`super`**:
- `super()` is a function that is used to call a method from the parent class.
- It is commonly used in method overriding to extend or modify the behavior of inherited methods.

**Example**:
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Animal sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call the constructor of the parent class
        self.breed = breed

    def speak(self):
        return f"{self.name} says Woof Woof"

# Create an object of the Dog class
dog = Dog("Buddy", "Golden Retriever")
print(dog.speak())  # Output: Buddy says Woof Woof
```

#### 5. Overriding

**Definition**:
Method overriding allows a derived class to provide a specific implementation of a method that is already defined in its base class.

**Example**:
```python
class Animal:
    def speak(self):
        return "Animal sound"

class Dog(Animal):
    def speak(self):
        return "Woof Woof"

# Create an object of the Dog class
dog = Dog()
print(dog.speak())  # Output: Woof Woof
```

**Using `super` with Overriding**:
```python
class Animal:
    def speak(self):
        return "Animal sound"

class Dog(Animal):
    def speak(self):
        base_sound = super().speak()  # Call the method from the parent class
        return f"{base_sound} and Woof Woof"

# Create an object of the Dog class
dog = Dog()
print(dog.speak())  # Output: Animal sound and Woof Woof
```

### Summary

- **Inheritance**: Allows a class to inherit attributes and methods from another class.
- **Types of Inheritance**: Single, multiple, multilevel, hierarchical, and hybrid.
- **`self`**: Reference to the current instance of the class.
- **`super`**: Function to call a method from the parent class.
- **Overriding**: Allows a derived class to provide a specific implementation of a method already defined in its base class.
