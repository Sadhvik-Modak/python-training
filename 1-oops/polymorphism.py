# Method Overriding
class Animal:
    def speak(self):
        return "Some generic sound"

    def internal_fn(self):
        # Some internal login
        pass

class Dog(Animal):
    def speak(self):
        return "Woof Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

# Method Overloading