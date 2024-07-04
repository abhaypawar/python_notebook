
# Data Types and Basic Operations in Python

This repository contains Python code that demonstrates fundamental concepts related to different data types in Python, including integers, floating-point numbers, strings, and booleans. The code also covers basic arithmetic operations, string manipulations, logical operations, and type checking.

## Table of Contents

- [Integers](#integers)
- [Floating-point Numbers](#floating-point-numbers)
- [Strings](#strings)
- [Booleans](#booleans)
- [Type Checking](#type-checking)

## Integers

Integers are whole numbers that can be positive, negative, or zero. The code demonstrates basic arithmetic operations with integers, such as addition, subtraction, multiplication, division, exponentiation, floor division, and modulus.

### Key Points:
- **Arithmetic Operations:** Basic mathematical operations.
- **Floor Division (`//`):** Divides and returns the largest whole number less than or equal to the result.
- **Modulus (`%`):** Returns the remainder of the division.

```python
num1 = 10
num2 = -5
addition = num1 + num2
```

## Floating-point Numbers

Floating-point numbers are numbers with a decimal point. The code shows arithmetic operations with floating-point numbers.

### Key Points:
- **Precision:** Floating-point numbers are represented with precision, which can sometimes lead to rounding errors.
- **Exponentiation:** Raising a number to the power of another.

```python
float1 = 3.14
float2 = -2.5
addition_float = float1 + float2
```

## Strings

Strings are sequences of characters enclosed in single or double quotes. The code includes various string operations such as concatenation, length calculation, case conversion, and some additional operations like finding substrings, replacing, splitting, and stripping characters.

### Key Points:
- **Concatenation:** Combining strings using `+`.
- **Case Conversion:** Changing the case of characters in a string using methods like `upper()` and `lower()`.
- **String Methods:** Methods such as `find()`, `replace()`, `split()`, and `strip()` for more advanced manipulations.

```python
name = "Alice"
message = 'Hello, World!'
concatenation_with_space = name + " " + message
```

## Booleans

Booleans represent one of two values: `True` or `False`. The code demonstrates logical operations with boolean values.

### Key Points:
- **Logical Operations:** `and`, `or`, and `not` for combining and negating boolean values.

```python
x = True
y = False
logical_and = x and y
```

## Type Checking

Type checking allows you to determine the type of a variable using the `type()` function.

### Key Points:
- **Dynamic Typing:** Python is dynamically typed, meaning the type of a variable is determined at runtime.

```python
print(type(num1))  # Output: <class 'int'>
```

## Insights and Lesser-known Facts

- **Floating-point Precision:** Due to the way floating-point numbers are stored, they can introduce precision errors in calculations. It is important to be aware of this when performing arithmetic operations with floats.
- **String Immutability:** Strings in Python are immutable, meaning once a string is created, it cannot be changed. Operations that seem to modify a string actually create a new string.
- **Boolean Operations Short-circuiting:** In logical operations, Python uses short-circuit evaluation. For example, in an `or` operation, if the first operand is `True`, Python will not evaluate the second operand.

This code serves as a basic introduction to these data types and operations, providing a foundation for more advanced programming concepts in Python.
```
