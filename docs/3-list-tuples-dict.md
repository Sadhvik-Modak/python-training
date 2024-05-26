# Session 4: Lists. Tuples and Dictoniaries


## 1. Sequence Types

Sequence types in Python include `str`, `list`, and `tuple`.

#### `str`
- Represents a sequence of characters (strings).

##### Methods and Operations:
- `+` (concatenation), `*` (repetition)
- `len()`, `str()`, `upper()`, `lower()`, `strip()`, `replace()`, `split()`, `join()`, `find()`, `count()`, `startswith()`, `endswith()`

##### Examples:
```python
name = "Alice"  # str

print(name.upper())          # Output: ALICE
print(name.lower())          # Output: alice
print(name.strip())          # Output: Alice
print(name.replace('A', 'a')) # Output: alice
print(name.split('i'))       # Output: ['Al', 'ce']
print('-'.join(['A', 'B']))  # Output: A-B
print(name.find('i'))        # Output: 2
print(name.count('i'))       # Output: 1
print(name.startswith('A'))  # Output: True
print(name.endswith('e'))    # Output: True
```

#### `list`
- Represents a mutable sequence of items.

##### Methods and Operations:
- `+` (concatenation), `*` (repetition)
- `len()`, `append()`, `extend()`, `insert()`, `remove()`, `pop()`, `clear()`, `index()`, `count()`, `sort()`, `reverse()`, `copy()`

##### Examples:
```python
numbers = [1, 2, 3]  # list

numbers.append(4)
print(numbers)             # Output: [1, 2, 3, 4]
numbers.extend([5, 6])
print(numbers)             # Output: [1, 2, 3, 4, 5, 6]
numbers.insert(0, 0)
print(numbers)             # Output: [0, 1, 2, 3, 4, 5, 6]
numbers.remove(3)
print(numbers)             # Output: [0, 1, 2, 4, 5, 6]
print(numbers.pop())       # Output: 6
print(numbers)             # Output: [0, 1, 2, 4, 5]
numbers.sort()
print(numbers)             # Output: [0, 1, 2, 4, 5]
numbers.reverse()
print(numbers)             # Output: [5, 4, 2, 1, 0]
print(numbers.index(4))    # Output: 1
print(numbers.count(2))    # Output: 1
```

#### `tuple`
- Represents an immutable sequence of items.

##### Methods and Operations:
- `+` (concatenation), `*` (repetition)
- `len()`, `index()`, `count()`

##### Examples:
```python
coordinates = (10, 20)  # tuple

print(len(coordinates))        # Output: 2
print(coordinates.index(20))   # Output: 1
print(coordinates.count(10))   # Output: 1
```

## 2. Mapping Type

#### `dict`
- Represents a collection of key-value pairs.

##### Methods and Operations:
- `len()`, `keys()`, `values()`, `items()`, `get()`, `update()`, `pop()`,

- `popitem()`, `clear()`, `copy()`, `setdefault()`

##### Examples:
```python
person = {"name": "Bob", "age": 25, "city": "New York"}  # dict

print(person.keys())           # Output: dict_keys(['name', 'age', 'city'])
print(person.values())         # Output: dict_values(['Bob', 25, 'New York'])
print(person.items())          # Output: dict_items([('name', 'Bob'), ('age', 25), ('city', 'New York')])
print(person.get("name"))      # Output: Bob
person.update({"age": 26})
print(person)                  # Output: {'name': 'Bob', 'age': 26, 'city': 'New York'}
person.pop("city")
print(person)                  # Output: {'name': 'Bob', 'age': 26}
person.setdefault("country", "USA")
print(person)                  # Output: {'name': 'Bob', 'age': 26, 'country': 'USA'}
```

## 3. Set Types

Set types in Python include `set` and `frozenset`.

#### `set`
- Represents an unordered collection of unique items.

##### Methods and Operations:
- `len()`, `add()`, `update()`, `remove()`, `discard()`, `pop()`, `clear()`, `union()`, `intersection()`, `difference()`, `symmetric_difference()`, `issubset()`, `issuperset()`, `copy()`

##### Examples:
```python
unique_numbers = {1, 2, 3, 3}  # set

print(unique_numbers)          # Output: {1, 2, 3}
unique_numbers.add(4)
print(unique_numbers)          # Output: {1, 2, 3, 4}
unique_numbers.update([5, 6])
print(unique_numbers)          # Output: {1, 2, 3, 4, 5, 6}
unique_numbers.remove(3)
print(unique_numbers)          # Output: {1, 2, 4, 5, 6}
unique_numbers.discard(2)
print(unique_numbers)          # Output: {1, 4, 5, 6}
unique_numbers.pop()
print(unique_numbers)          # Output: {4, 5, 6}
print(unique_numbers.union({7, 8}))               # Output: {4, 5, 6, 7, 8}
print(unique_numbers.intersection({5, 6, 7}))     # Output: {5, 6}
print(unique_numbers.difference({5}))             # Output: {4, 6}
print(unique_numbers.symmetric_difference({4}))  # Output: {5, 6, 4}
```

#### `frozenset`
- Represents an immutable set.

##### Methods and Operations:
- Similar to `set`, but immutable.

##### Examples:
```python
frozen_numbers = frozenset([1, 2, 3, 3])  # frozenset

print(frozen_numbers)                     # Output: frozenset({1, 2, 3})
print(frozen_numbers.union({4, 5}))       # Output: frozenset({1, 2, 3, 4, 5})
print(frozen_numbers.intersection({2}))   # Output: frozenset({2})
print(frozen_numbers.difference({3}))     # Output: frozenset({1, 2})
print(frozen_numbers.symmetric_difference({1}))  # Output: frozenset({2, 3})
```

### Additional List Methods

Lists are highly flexible and come with various methods to handle complex operations.

#### Examples:
```python
numbers = [1, 2, 3, 4, 5]

numbers.append(6)
print(numbers)  # Output: [1, 2, 3, 4, 5, 6]

numbers.extend([7, 8])
print(numbers)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]

numbers.insert(0, 0)
print(numbers)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8]

numbers.remove(4)
print(numbers)  # Output: [0, 1, 2, 3, 5, 6, 7, 8]

popped_number = numbers.pop()
print(popped_number)  # Output: 8
print(numbers)        # Output: [0, 1, 2, 3, 5, 6, 7]

numbers.sort()
print(numbers)  # Output: [0, 1, 2, 3, 5, 6, 7]

numbers.reverse()
print(numbers)  # Output: [7, 6, 5, 3, 2, 1, 0]

index_of_five = numbers.index(5)
print(index_of_five)  # Output: 2

count_of_two = numbers.count(2)
print(count_of_two)  # Output: 1

copied_numbers = numbers.copy()
print(copied_numbers)  # Output: [7, 6, 5, 3, 2, 1, 0]

numbers.clear()
print(numbers)  # Output: []
```

