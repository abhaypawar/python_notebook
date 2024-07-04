############################################################################### 1. Recursive Function: Factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Calculate factorial of 5
result_factorial = factorial(5)
print("Factorial of 5:", result_factorial)  # Output: 120


############################################################################### 2. Function as Argument (Higher-Order Function)
def apply_operation(operation, x, y):
    return operation(x, y)

# Define operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

# Apply different operations
result_add = apply_operation(add, 5, 3)
result_subtract = apply_operation(subtract, 10, 7)

print("Result of adding:", result_add)         # Output: 8
print("Result of subtracting:", result_subtract)  # Output: 3


############################################################################### 3. Lambda Function: Square and Multiply
square = lambda x: x ** 2
multiply = lambda x, y: x * y

result_square = square(5)
result_multiply = multiply(3, 4)

print("Square of 5:", result_square)      # Output: 25
print("Product of 3 and 4:", result_multiply)  # Output: 12


############################################################################### 4. Global vs Local Variables
global_var = 10  # Global variable

def modify_global():
    global global_var
    global_var += 5

def local_example():
    local_var = 20  # Local variable
    print("Local variable inside function:", local_var)

# Modify global variable
modify_global()
print("Modified global variable:", global_var)  # Output: 15

# Uncommenting the line below would raise a NameError because local_var is not accessible outside local_example():
# print("Trying to access local_var outside function:", local_var)

# Call local_example function to demonstrate local variable scope
local_example()
