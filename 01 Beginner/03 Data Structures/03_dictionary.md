
# Python Dictionaries

This repository contains a Python script that demonstrates various operations on dictionaries in Python. It covers creating dictionaries, accessing values using keys, adding and modifying key-value pairs, removing key-value pairs, checking for key existence, getting the length of the dictionary, and iterating over key-value pairs.

## Table of Contents

- [1. Creating a dictionary](#1-creating-a-dictionary)
- [2. Accessing values in a dictionary using keys](#2-accessing-values-in-a-dictionary-using-keys)
- [3. Adding new key-value pairs to the dictionary](#3-adding-new-key-value-pairs-to-the-dictionary)
- [4. Modifying values in the dictionary](#4-modifying-values-in-the-dictionary)
- [5. Removing a key-value pair from the dictionary](#5-removing-a-key-value-pair-from-the-dictionary)
- [6. Checking if a key exists in the dictionary](#6-checking-if-a-key-exists-in-the-dictionary)
- [7. Length of the dictionary](#7-length-of-the-dictionary)
- [8. Iterating over keys and values in the dictionary](#8-iterating-over-keys-and-values-in-the-dictionary)

## 1. Creating a dictionary

A dictionary in Python is defined using curly braces `{}` and consists of key-value pairs.

```python
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
```

## 2. Accessing values in a dictionary using keys

You can access values in a dictionary using keys.

```python
print("Name:", my_dict['name'])  # Output: Alice
print("Age:", my_dict['age'])  # Output: 30
```

## 3. Adding new key-value pairs to the dictionary

You can add new key-value pairs to a dictionary using assignment.

```python
my_dict['email'] = 'alice@example.com'
print("Updated dictionary:", my_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'email': 'alice@example.com'}
```

## 4. Modifying values in the dictionary

You can modify the value associated with a key in a dictionary.

```python
my_dict['age'] = 35
print("Modified dictionary:", my_dict)  # Output: {'name': 'Alice', 'age': 35, 'city': 'New York', 'email': 'alice@example.com'}
```

## 5. Removing a key-value pair from the dictionary

You can remove a key-value pair from a dictionary using the `pop()` method.

```python
removed_value = my_dict.pop('city')
print("Removed value:", removed_value)  # Output: New York
print("Updated dictionary:", my_dict)  # Output: {'name': 'Alice', 'age': 35, 'email': 'alice@example.com'}
```

## 6. Checking if a key exists in the dictionary

You can check if a specific key exists in a dictionary using the `in` keyword.

```python
print("Is 'email' in the dictionary?", 'email' in my_dict)  # Output: True
```

## 7. Length of the dictionary

You can find the number of key-value pairs in a dictionary using the `len()` function.

```python
print("Length of the dictionary:", len(my_dict))  # Output: 3
```

## 8. Iterating over keys and values in the dictionary

You can iterate over all keys and values in a dictionary using a `for` loop and the `items()` method.

```python
print("\nIterating over keys and values in the dictionary:")
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")
```

### Insights and Lesser-known Facts

1. **Dictionary Keys**: Keys in a dictionary must be unique and immutable (strings, numbers, or tuples).
   
2. **Dictionary Methods**: Dictionaries provide various methods such as `keys()`, `values()`, and `items()` for accessing keys, values, and key-value pairs respectively.

3. **Dictionary Memory Usage**: Dictionaries consume more memory than lists due to hash tables used for key lookup.

4. **Dictionary Views**: Views (`dict_keys`, `dict_values`, `dict_items`) provide dynamic views of the dictionary's keys, values, and items.

5. **Dictionary Comprehensions**: Similar to list comprehensions, dictionary comprehensions allow concise creation of dictionaries from iterable sequences.

This README provides an overview of basic operations on dictionaries in Python and introduces some lesser-known facts about their usage and characteristics.
