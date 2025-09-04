
1. **Arguments basics** (positional vs keyword).
2. **Why `*args` and `**kwargs` exist** (packing/unpacking).
3. **Decorators basics** (with these arguments).
4. **Each type of decorator** (with code + explanation).

---

# 🔹 1. Arguments in Python

## (a) Positional Arguments

* Passed **by order**.
* Example:

```python
def greet(name, age):
    print(f"My name is {name}, I am {age} years old.")

# Calling with positional arguments (order matters)
greet("Alice", 25)   # ✅ Works
greet(25, "Alice")   # ❌ Wrong meaning (age and name swapped)
```

---

## (b) Keyword Arguments

* Passed **by name**.
* Example:

```python
def greet(name, age):
    print(f"My name is {name}, I am {age} years old.")

# Calling with keyword arguments (order does NOT matter)
greet(age=25, name="Alice")  # ✅ Works fine
```

---

## (c) Mixing Positional and Keyword

* Positional must come **before** keyword.

```python
def add(a, b, c):
    return a + b + c

print(add(1, 2, 3))           # ✅ Positional
print(add(a=1, b=2, c=3))     # ✅ Keyword
print(add(1, b=2, c=3))       # ✅ Mixed
# print(add(a=1, 2, 3))       # ❌ SyntaxError: positional after keyword
```

---

# 🔹 2. `*args` and `**kwargs`

These make functions flexible.

## (a) `*args` (tuple of positional arguments)

```python
def demo(*args):
    print("Positional args:", args)

demo(1, 2, 3)  # ✅ Packs into tuple → (1, 2, 3)
```

---

## (b) `**kwargs` (dict of keyword arguments)

```python
def demo(**kwargs):
    print("Keyword args:", kwargs)

demo(name="Alice", age=25)  # ✅ Packs into dict → {'name': 'Alice', 'age': 25}
```

---

## (c) Both together

```python
def demo(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)

demo(10, 20, user="Bob", active=True)
# ✅ Positional: (10, 20)
# ✅ Keyword: {'user': 'Bob', 'active': True}
```

---

## (d) Unpacking with `*` and `**`

```python
def add(a, b, c):
    return a + b + c

nums = [1, 2, 3]
print(add(*nums))   # ✅ Equivalent to add(1, 2, 3)

data = {"a": 1, "b": 2, "c": 3}
print(add(**data))  # ✅ Equivalent to add(a=1, b=2, c=3)
```

---

# 🔹 3. Basics of Decorators

A decorator is **a function that wraps another function**.

```python
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function runs")
        result = func(*args, **kwargs)   # Run original function
        print("After function runs")
        return result
    return wrapper

@decorator
def greet(name):
    print(f"Hello {name}")

greet("Alice")
```

✅ Output:

```
Before function runs
Hello Alice
After function runs
```

---

# 🔹 4. Types of Decorators

---

## (a) Function Decorators

```python
def log(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log
def add(a, b):
    return a + b

print(add(2, 3))  # ✅ Logs and returns 5
```

---

## (b) Method Decorators (inside classes)

```python
def log_method(func):
    def wrapper(self, *args, **kwargs):
        print(f"Method {func.__name__} called on {self}")
        return func(self, *args, **kwargs)
    return wrapper

class User:
    def __init__(self, name):
        self.name = name

    @log_method
    def greet(self, greeting="Hello"):
        print(f"{greeting}, I am {self.name}")

u = User("Alice")
u.greet("Hi")
```

✅ Output:

```
Method greet called on <__main__.User object at 0x...>
Hi, I am Alice
```

---

## (c) Built-in Decorators

### `@staticmethod`

```python
class Math:
    @staticmethod
    def square(x):
        return x * x

print(Math.square(4))  # ✅ Works without creating object
```

---

### `@classmethod`

```python
class Person:
    def __init__(self, name):
        self.name = name

    @classmethod
    def guest(cls):
        return cls("Guest")

p = Person.guest()
print(p.name)  # Guest
```

---

### `@property`

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 3.14 * self.radius ** 2

c = Circle(5)
print(c.area)  # ✅ Looks like attribute, not method
```

---

## (d) Decorators with Arguments

```python
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hi():
    print("Hi!")

say_hi()
```

✅ Output:

```
Hi!
Hi!
Hi!
```

---

## (e) Multiple Decorators (stacked)

```python
def star(func):
    def wrapper(*args, **kwargs):
        print("*****")
        func(*args, **kwargs)
        print("*****")
    return wrapper

def smile(func):
    def wrapper(*args, **kwargs):
        print(":)")
        func(*args, **kwargs)
        print(":)")
    return wrapper

@star
@smile
def greet(name):
    print(f"Hello {name}")

greet("Bob")
```

✅ Output:

```
*****
:)
Hello Bob
:)
*****
```

---

✅ Now you know:

* Positional vs keyword arguments.
* `*args` & `**kwargs` (packing/unpacking).
* Basic and advanced decorators.
* Types: function decorators, method decorators, built-in decorators, decorator arguments, multiple decorators.
