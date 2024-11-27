Decorators in Python are versatile tools used for modifying or enhancing the behavior of functions, methods, or classes. Broadly, they can be categorized into the following types based on their purpose and usage:

---

### 1. **Function Decorators**
   - These are used to modify or extend the behavior of functions.
   - They take a function as input and return a modified or wrapped version of it.

   **Example:**
   ```python
   def uppercase_decorator(func):
       def wrapper():
           result = func()
           return result.upper()
       return wrapper

   @uppercase_decorator
   def greet():
       return "hello"
   
   print(greet())  # Output: "HELLO"
   ```

---

### 2. **Method Decorators**
   - Specifically designed to modify or extend the behavior of class methods.
   - Can be applied to instance methods, class methods, or static methods.

   **Example:**
   ```python
   def log_decorator(func):
       def wrapper(*args, **kwargs):
           print(f"Calling method {func.__name__}")
           return func(*args, **kwargs)
       return wrapper

   class MyClass:
       @log_decorator
       def method(self):
           print("Method called")
   
   obj = MyClass()
   obj.method()
   # Output:
   # Calling method method
   # Method called
   ```

---

### 3. **Class Decorators**
   - These are used to modify or extend the behavior of an entire class.
   - The decorator takes a class as input and returns a modified class.

   **Example:**
   ```python
   def add_method_decorator(cls):
       cls.new_method = lambda self: "New method added!"
       return cls

   @add_method_decorator
   class MyClass:
       pass

   obj = MyClass()
   print(obj.new_method())  # Output: "New method added!"
   ```

---

### 4. **Built-in Decorators**
   - Python provides several built-in decorators for specific use cases:
     - **@staticmethod**: Defines a method that doesn’t require access to instance or class-specific data.
     - **@classmethod**: Defines a method that takes the class (`cls`) as its first argument.
     - **@property**: Defines a method that can be accessed like an attribute.

   **Example:**
   ```python
   class MyClass:
       @staticmethod
       def static_method():
           return "I am a static method"

       @classmethod
       def class_method(cls):
           return f"I am a class method of {cls.__name__}"

       @property
       def greet(self):
           return "Hello, I am a property!"
   
   obj = MyClass()
   print(obj.static_method())  # Output: "I am a static method"
   print(MyClass.class_method())  # Output: "I am a class method of MyClass"
   print(obj.greet)  # Output: "Hello, I am a property!"
   ```

---

### 5. **Chained Decorators**
   - When multiple decorators are applied to a single function or method, they are executed in order, from the bottom up (closest to the function runs first).

   **Example:**
   ```python
   def decorator_one(func):
       def wrapper():
           print("Decorator One")
           func()
       return wrapper

   def decorator_two(func):
       def wrapper():
           print("Decorator Two")
           func()
       return wrapper

   @decorator_one
   @decorator_two
   def my_function():
       print("Hello!")

   my_function()
   # Output:
   # Decorator One
   # Decorator Two
   # Hello!
   ```

---

### 6. **Parameter-based Decorators**
   - Decorators that accept additional arguments to customize their behavior.

   **Example:**
   ```python
   def repeat_decorator(times):
       def decorator(func):
           def wrapper(*args, **kwargs):
               for _ in range(times):
                   func(*args, **kwargs)
           return wrapper
       return decorator

   @repeat_decorator(3)
   def greet():
       print("Hello!")

   greet()
   # Output:
   # Hello!
   # Hello!
   # Hello!
   ```

---

### 7. **Custom Decorators**
   - Tailored for specific use cases like logging, timing, access control, memoization, etc.

   **Example:**
   - **Logging Decorator:**
     ```python
     def logging_decorator(func):
         def wrapper(*args, **kwargs):
             print(f"Function {func.__name__} called with args: {args}, kwargs: {kwargs}")
             return func(*args, **kwargs)
         return wrapper

     @logging_decorator
     def add(a, b):
         return a + b

     print(add(5, 10))
     # Output:
     # Function add called with args: (5, 10), kwargs: {}
     # 15
     ```

   - **Timing Decorator:**
     ```python
     import time

     def timing_decorator(func):
         def wrapper(*args, **kwargs):
             start = time.time()
             result = func(*args, **kwargs)
             end = time.time()
             print(f"{func.__name__} executed in {end - start:.4f} seconds")
             return result
         return wrapper

     @timing_decorator
     def slow_function():
         time.sleep(2)
         print("Function complete")

     slow_function()
     # Output:
     # Function complete
     # slow_function executed in 2.0001 seconds
     ```

---

These types illustrate how decorators can be applied at various levels, making them a powerful feature in Python for enhancing code modularity and readability.
