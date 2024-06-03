text = "abc abc abc"

print(text)
print(text.strip())          # Output: "Hello, World!"
print(text.rstrip())         # Output: "  Hello, World!"
print(text.lstrip())         # Output: "Hello, World!  "
print(text.replace("World", "Python"))  # Output: "  Hello, Python!  "
# print(text.split(','))       # Output: ['  Hello', ' World!  ']
print(text.lower())          # Output: "  hello, world!  "
print(text.upper())          # Output: "  HELLO, WORLD!  "
print(text.title())          # Output: "  Hello, World!  "

print(text.startswith(" "))  # Output: True
print(text.endswith("!  "))  # Output: True

print(text.find("l"))    # Output: 9

print(text.count("c a"))       # Output: 3
