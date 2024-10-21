

# Exploring Python Function Concepts

This Python script explores several fundamental concepts related to functions in Python, including recursive functions, functions as arguments (higher-order functions), lambda functions, and the scope of global vs. local variables.

## Contents

1. [Recursive Function: Factorial](#1-recursive-function-factorial)
2. [Function as Argument (Higher-Order Function)](#2-function-as-argument-higher-order-function)
3. [Lambda Function: Square and Multiply](#3-lambda-function-square-and-multiply)
4. [Global vs. Local Variables](#4-global-vs-local-variables)

---

### 1. Recursive Function: Factorial

The script begins with a recursive function to calculate the factorial of a number. Recursive functions call themselves to solve smaller instances of the same problem until a base case is reached.

Example:
```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

result_factorial = factorial(5)
print("Factorial of 5:", result_factorial)  # Output: 120
```

### 2. Function as Argument (Higher-Order Function)

Python supports higher-order functions, where functions can be passed as arguments to other functions. This provides flexibility and reusability in code.

Example:
```python
def apply_operation(operation, x, y):
    return operation(x, y)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

result_add = apply_operation(add, 5, 3)
result_subtract = apply_operation(subtract, 10, 7)

print("Result of adding:", result_add)         # Output: 8
print("Result of subtracting:", result_subtract)  # Output: 3
```

### 3. Lambda Function: Square and Multiply

Lambda functions are anonymous functions defined with the `lambda` keyword. They are useful for simple operations without the need for a formal function definition.

Example:
```python
square = lambda x: x ** 2
multiply = lambda x, y: x * y

result_square = square(5)
result_multiply = multiply(3, 4)

print("Square of 5:", result_square)      # Output: 25
print("Product of 3 and 4:", result_multiply)  # Output: 12
```

### 4. Global vs. Local Variables

Python distinguishes between global and local variables within functions. The `global` keyword is used to modify global variables inside functions, while local variables are scoped to the function they are defined in.

Example:
```python
global_var = 10  # Global variable

def modify_global():
    global global_var
    global_var += 5

def local_example():
    local_var = 20  # Local variable
    print("Local variable inside function:", local_var)

modify_global()
print("Modified global variable:", global_var)  # Output: 15

local_example()
# Uncommenting the line below would raise a NameError because local_var is not accessible outside local_example():
# print("Trying to access local_var outside function:", local_var)
```

---

### Lesser-Known Concepts and Facts

- **Recursive Functions**: They are useful for solving problems that can be broken down into smaller, similar problems, but they can lead to stack overflow errors if not implemented with a base case properly.
  
- **Functions as Arguments**: Python's support for higher-order functions allows for powerful and flexible code structures, promoting modularity and code reuse.
  
- **Lambda Functions**: These are handy for short and concise operations where defining a full function may be unnecessary or less readable.
  
- **Global vs. Local Variables**: Understanding variable scope is crucial; modifying global variables inside functions using the `global` keyword and recognizing local variables are scoped within their defining function.



### 5. **Memoization**  
   **Optimizing Recursive Functions**  
   Memoization is a technique to optimize recursive functions by storing previously computed results. This can significantly improve performance for functions with overlapping subproblems, such as calculating Fibonacci numbers.
   ```python
   def fibonacci(n, memo={}):
       if n in memo:
           return memo[n]
       if n <= 1:
           return n
       memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
       return memo[n]

   print(fibonacci(10))  # Output: 55
   ```

### 6. **Function Decorators**  
   **Enhancing Functionality with Decorators**  
   Decorators allow you to modify or enhance the behavior of functions without changing their code. They are often used for logging, access control, and memoization.
   ```python
   def timer_decorator(func):
       import time
       def wrapper(*args, **kwargs):
           start_time = time.time()
           result = func(*args, **kwargs)
           end_time = time.time()
           print(f"Function '{func.__name__}' executed in {end_time - start_time:.4f} seconds.")
           return result
       return wrapper

   @timer_decorator
   def compute_square(n):
       return n * n

   print(compute_square(1000000))  # Outputs execution time along with the result
   ```

### 7. **Context Managers**  
   **Managing Resources with `with` Statement**  
   Context managers allow you to allocate and release resources precisely when you want to. The `with` statement simplifies exception handling by encapsulating common preparation and cleanup tasks.
   ```python
   class FileManager:
       def __init__(self, filename):
           self.filename = filename

       def __enter__(self):
           self.file = open(self.filename, 'w')
           return self.file

       def __exit__(self, exc_type, exc_value, traceback):
           self.file.close()

   with FileManager('test.txt') as f:
       f.write("Hello, World!")

   # The file is automatically closed after exiting the with block.
   ```

### 8. **Generator Functions**  
   **Using `yield` to Create Generators**  
   Generator functions allow you to declare a function that behaves like an iterator. They use the `yield` statement to produce a series of values lazily, meaning they can generate values on the fly and save memory.
   ```python
   def count_up_to(max):
       count = 1
       while count <= max:
           yield count
           count += 1

   for number in count_up_to(5):
       print(number)  # Output: 1, 2, 3, 4, 5
   ```

### 9. **Callable Objects**  
   **Creating Functions with Classes**  
   In Python, you can create callable objects by defining a `__call__` method in a class. This allows instances of the class to be called like functions.
   ```python
   class Adder:
       def __init__(self, value):
           self.value = value

       def __call__(self, x):
           return self.value + x

   add_five = Adder(5)
   print(add_five(10))  # Output: 15
   ```

### 10. **Using Functions in Multithreading or Multiprocessing**  
    **Executing Functions Concurrently**  
    Python's `threading` and `multiprocessing` libraries allow you to run functions concurrently, enabling efficient resource utilization and improved performance in I/O-bound or CPU-bound tasks.
    ```python
    import threading

    def print_numbers():
        for i in range(5):
            print(i)

    thread = threading.Thread(target=print_numbers)
    thread.start()
    thread.join()  # Wait for the thread to finish
    ```

---


