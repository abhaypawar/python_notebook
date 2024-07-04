################################################################################### 1. Defining Functions
print("1. Defining Functions")

# Basic function definition without arguments or return value
def greet():
    print("Hello, World!")

greet()

# Function with arguments and return value
def add_numbers(a, b):
    return a + b

result = add_numbers(3, 5)
print("Result of adding 3 and 5:", result)

# Function with default argument
def greet_person(name="Guest"):
    print(f"Hello, {name}!")

greet_person("Alice")
greet_person()  # Uses default argument

# Function with variable-length arguments
def calculate_sum(*args):
    return sum(args)

sum_result = calculate_sum(1, 2, 3, 4, 5)
print("Sum of numbers:", sum_result)

print()

################################################################################### 2. Passing Arguments to Functions
print("2. Passing Arguments to Functions")

# Positional arguments
def greet_with_message(message, name):
    print(f"{message}, {name}!")

greet_with_message("Hi", "Alice")

# Keyword arguments
def greet_with_defaults(message="Hello", name="Guest"):
    print(f"{message}, {name}!")

greet_with_defaults()
greet_with_defaults("Hi")
greet_with_defaults(name="Bob")

# Mixed positional and keyword arguments
def describe_person(name, age, city="Unknown"):
    print(f"{name} is {age} years old and lives in {city}.")

describe_person("Alice", 30)
describe_person("Bob", 25, "New York")

print()

################################################################################### 3. Returning Values from Functions
print("3. Returning Values from Functions")

# Function returning a single value
def multiply(a, b):
    return a * b

product = multiply(4, 5)
print("Product of 4 and 5:", product)

# Function returning multiple values using tuple unpacking
def operate_numbers(x, y):
    return x + y, x - y, x * y, x / y

addition, subtraction, multiplication, division = operate_numbers(10, 5)
print("Results of operations:")
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)

# Returning different data types
def return_different_types():
    return 1, "Hello", [1, 2, 3]

result_int, result_str, result_list = return_different_types()
print("Different types returned:", result_int, result_str, result_list)

print()

# Additional concepts can be explored such as:
# - Recursive functions
# - Functions as arguments (higher-order functions)
# - Anonymous functions (lambda functions)
# - Global vs local variables in functions
