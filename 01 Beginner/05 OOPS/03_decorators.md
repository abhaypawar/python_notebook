# **Python Decorators and Types of Decorators**

## **What are Decorators?**
- **Definition**: A decorator in Python is a function that modifies the behavior of another function or method. It allows you to "wrap" a function with additional functionality.
- **Syntax**: Decorators are applied using the `@decorator_name` syntax above the function definition.

---

## **Types of Decorators**
Decorators in Python can be categorized based on their usage:

### **1. Function Decorators**
- Modify or enhance the behavior of functions.
- Common examples: `@staticmethod`, `@classmethod`.

---

### **2. Class Decorators**
- Modify or enhance the behavior of classes.
- Example: Custom decorators that add attributes or modify methods within a class.

---

### **3. Built-in Method Decorators**
These are specific to classes and methods, such as `@staticmethod`, `@classmethod`, and `@property`.

---

## **Built-in Method Decorators in Detail**

### **1. `@staticmethod`**
- **Purpose**: Defines a method that belongs to the class, not any specific instance.
- **Key Points**:
  - No access to `self` (instance) or `cls` (class).
  - Useful for utility functions that do not depend on instance or class-level data.
- **Example**:
  ```python
  class Example:
      @staticmethod
      def greet(name):
          return f"Hello, {name}!"

  # Usage
  print(Example.greet("Alice"))  # Output: Hello, Alice!
  ```
- **Use Case**: Independent functions related to the class (e.g., generating random IDs).

---

### **2. `@classmethod`**
- **Purpose**: Defines a method that belongs to the class and has access to the class itself via `cls`.
- **Key Points**:
  - Can access class-level variables and methods.
  - Commonly used for creating alternate constructors.
- **Example**:
  ```python
  class Example:
      count = 0

      @classmethod
      def increment(cls):
          cls.count += 1

  # Usage
  Example.increment()
  print(Example.count)  # Output: 1
  ```

---

### **3. `@property`**
- **Purpose**: Creates a read-only attribute or a dynamically computed property.
- **Key Points**:
  - Allows access to a method like it’s an attribute (no parentheses required).
  - Often used for encapsulation and computed attributes.
- **Example**:
  ```python
  class Example:
      def __init__(self, name, age):
          self.name = name
          self.age = age

      @property
      def info(self):
          return f"{self.name} is {self.age} years old."

  # Usage
  obj = Example("Alice", 30)
  print(obj.info)  # Output: Alice is 30 years old.
  ```

---

## **Custom Decorators**
You can create your own decorators to add specific functionality.

### **Structure of a Custom Decorator**
- A decorator is typically a function that takes a function as input and returns a modified version of that function.
```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Function is being called!")
        result = func(*args, **kwargs)
        print("Function has been executed.")
        return result
    return wrapper

@my_decorator
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
```
**Output**:
```
Function is being called!
Hello, Alice!
Function has been executed.
```

---

## **Comparison of Built-in Decorators**

| Decorator      | Purpose                                    | Can Access `self`? | Can Access `cls`? | Usage Example         |
|----------------|--------------------------------------------|--------------------|-------------------|-----------------------|
| `@staticmethod` | Defines a utility method                  | ❌                 | ❌                | Helper functions      |
| `@classmethod`  | Defines a method that works at class level | ❌                 | ✅                | Alternate constructors|
| `@property`     | Defines a read-only or computed attribute | ✅                 | ❌                | Dynamic properties    |

---

## **Use Case Example: BankAccount Class**

```python
class BankAccount:
    bank_name = "MyBank"

    def __init__(self, account_holder, initial_balance=0):
        self.holder = account_holder
        self.balance = initial_balance

    @staticmethod
    def generate_account_number():
        import random
        return random.randint(10000, 99999)

    @property
    def account_info(self):
        return f"Account Holder: {self.holder}, Balance: ${self.balance}"

# Usage
account = BankAccount("John Doe", 1000)
print(account.account_info)  # Output: Account Holder: John Doe, Balance: $1000
print(account.generate_account_number())  # Example Output: 12345
```

---

## **Advantages of Decorators**
1. Clean and reusable code for common functionalities.
2. Encapsulation and abstraction.
3. Enhances modularity by separating logic into layers.

## **Conclusion**
Decorators are a powerful tool for enhancing and customizing the behavior of functions and methods. Built-in decorators like `@staticmethod`, `@classmethod`, and `@property` are widely used in Python for utility, class-level methods, and computed attributes. Understanding decorators helps in writing clean, maintainable, and Pythonic code!
