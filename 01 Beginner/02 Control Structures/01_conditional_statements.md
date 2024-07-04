
# Python Conditional Statements Exploration

This repository contains a Python script that explores various methods of using conditional statements in Python. It covers basic `if` statements, `if-elif-else` chains, nested `if` statements, and more advanced techniques such as the ternary conditional operator and the `match` statement introduced in Python 3.10.

## Table of Contents

- [1. Simple if statement](#1-simple-if-statement)
- [2. if-elif-else statement](#2-if-elif-else-statement)
- [3. Nested if statements](#3-nested-if-statements)
- [4. Ternary Conditional Operator](#4-ternary-conditional-operator)
- [5. Conditional Expressions with Boolean Operators](#5-conditional-expressions-with-boolean-operators)
- [6. Using match statements (Python 3.10 and above)](#6-using-match-statements-python-310-and-above)
- [7. Logical Operations](#7-logical-operations)
- [8. Membership Testing with in keyword](#8-membership-testing-with-in-keyword)
- [Insights and Lesser-known Facts](#insights-and-lesser-known-facts)

## 1. Simple if statement

The most basic way to use conditionals in Python.

```python
num = 10
if num > 0:
    print("Positive number")
```

## 2. if-elif-else statement

An `if-elif-else` chain to handle multiple conditions.

```python
num = -5
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")
```

## 3. Nested if statements

Nesting `if` statements to handle more complex logic.

```python
num = 15
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")
```

## 4. Ternary Conditional Operator

A shorthand for simple `if-else` statements.

```python
num = 7
result = "Positive number" if num > 0 else "Non-positive number"
print("Ternary Conditional Operator Result:", result)
```

## 5. Conditional Expressions with Boolean Operators

Combining multiple conditions using `and` and `or`.

```python
a = 10
b = 5
if a > 5 and b > 5:
    print("Both numbers are greater than 5")
elif a > 5 or b > 5:
    print("At least one number is greater than 5")
else:
    print("Neither number is greater than 5")
```

## 6. Using match statements (Python 3.10 and above)

Pattern matching, similar to switch-case statements in other languages.

```python
num = 2
match num:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case _:
        print("Other number")
```

## 7. Logical Operations

Using `if` statements with logical operations like modulus to check even or odd numbers.

```python
num = 12
if num % 2 == 0 and num > 10:
    print("Number is even and greater than 10")
elif num % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")
```

## 8. Membership Testing with in keyword

Using the `in` keyword for membership testing.

```python
char = 'a'
vowels = 'aeiou'
if char in vowels:
    print(f"'{char}' is a vowel")
else:
    print(f"'{char}' is a consonant")
```

## Insights and Lesser-known Facts

1. **Chained Comparisons:** Python allows chained comparisons, which can make conditions more concise and readable. For example, `if 0 < x < 10:` checks if `x` is between 0 and 10.

2. **Implicit Boolean Conversion:** Python can implicitly convert values to `bool`. Non-zero numbers, non-empty strings, and non-empty containers are considered `True`, while zero, empty strings, and empty containers are `False`.

3. **Short-circuit Evaluation:** In Boolean expressions with `and` and `or`, Python uses short-circuit evaluation. It stops evaluating as soon as the result is determined. For example, in `A and B`, if `A` is `False`, `B` is not evaluated.

4. **Conditional Expressions (Ternary Operator):** Python’s ternary operator is a concise way to return one of two values based on a condition. It is written as `x if condition else y`.

5. **Using `assert` for Conditional Testing:** The `assert` statement is a debugging aid that tests a condition. If the condition is `False`, it raises an `AssertionError` with an optional message.

6. **Pattern Matching (`match` statement):** Introduced in Python 3.10, `match` statements provide a way to perform pattern matching, similar to switch-case statements in other languages. It can be used for matching values, types, and even destructuring.

7. **`in` keyword for Membership Testing:** The `in` keyword is very powerful and can be used to check for membership in strings, lists, tuples, sets, and dictionaries.

This code provides a comprehensive exploration of different ways to use conditional statements in Python, offering a solid foundation for understanding and utilizing conditionals in your programs.
```

