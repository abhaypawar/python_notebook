# Python Intermediate Guide

## 1. File Handling

### 1.1 Basic File Operations

#### Opening Files
```python
# Different ways to open files
file1 = open('example.txt', 'r')  # Read mode
file2 = open('example.txt', 'w')  # Write mode
file3 = open('example.txt', 'a')  # Append mode
file4 = open('example.txt', 'r+')  # Read and write mode
```

#### Reading Files
```python
# Reading entire file
with open('example.txt', 'r') as file:
    content = file.read()  # Read entire file
    print(content)

# Reading line by line
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())  # strip() removes newline characters

# Reading specific number of characters
with open('example.txt', 'r') as file:
    partial_content = file.read(50)  # Read first 50 characters
```

#### Writing Files
```python
# Writing to a file
with open('output.txt', 'w') as file:
    file.write('Hello, World!')  # Write a single string
    file.writelines(['Line 1\n', 'Line 2\n'])  # Write multiple lines

# Appending to a file
with open('output.txt', 'a') as file:
    file.write('\nNew content')
```

#### Working with CSV Files
```python
import csv

# Reading CSV
with open('data.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        print(row)

# Writing CSV
with open('output.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Name', 'Age', 'City'])
    csv_writer.writerows([
        ['Alice', 30, 'New York'],
        ['Bob', 25, 'San Francisco']
    ])
```

### 1.2 Advanced File Handling
```python
# Context managers
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

# Using custom context manager
with FileManager('custom.txt', 'w') as file:
    file.write('Custom file management')
```

## 2. Error Handling

### 2.1 Basic Exception Handling
```python
try:
    x = int(input("Enter a number: "))
    result = 10 / x
except ValueError:
    print("Invalid input. Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print("No exceptions occurred")
finally:
    print("Execution completed")
```

### 2.2 Custom Exceptions
```python
class CustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def validate_age(age):
    if age < 0:
        raise CustomError("Age cannot be negative")
    return age

try:
    user_age = validate_age(-5)
except CustomError as ce:
    print(ce)
```

### 2.3 Logging Exceptions
```python
import logging

logging.basicConfig(
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s: %(message)s',
    filename='error_log.txt'
)

def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        logging.error(f"Division by zero: {e}")
        return None
    return result
```

## 3. Modules and Packages

### 3.1 Creating Modules
```python
# math_operations.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# main.py
import math_operations as mo
print(mo.add(5, 3))
```

### 3.2 Package Structure
```
my_package/
│
├── __init__.py
├── module1.py
└── module2.py
```

### 3.3 Standard Library Exploration
```python
import math
import random
import datetime
import json

# Math operations
print(math.sqrt(16))
print(math.pi)

# Random generation
print(random.randint(1, 10))
print(random.choice(['apple', 'banana', 'cherry']))

# Date and time
current_time = datetime.datetime.now()
print(current_time)

# JSON handling
data = {'name': 'Alice', 'age': 30}
json_string = json.dumps(data)
parsed_data = json.loads(json_string)
```

### 3.4 Virtual Environments
```bash
# Creating virtual environment
python -m venv myenv

# Activating virtual environment
# Windows
myenv\Scripts\activate
# macOS/Linux
source myenv/bin/activate

# Installing packages
pip install requests pandas numpy
```

## 4. Object-Oriented Programming

### 4.1 Basic Class Definition
```python
class Person:
    # Class variable
    species = 'Human'
    
    # Constructor
    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age
    
    # Instance method
    def introduce(self):
        return f"Hi, I'm {self.name}"

# Creating objects
person1 = Person("Alice", 30)
print(person1.introduce())
```

### 4.2 Inheritance
```python
class Employee(Person):
    def __init__(self, name, age, company):
        super().__init__(name, age)
        self.company = company
    
    def work_info(self):
        return f"{self.name} works at {self.company}"

emp = Employee("Bob", 35, "Tech Corp")
print(emp.work_info())
```

### 4.3 Polymorphism
```python
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

# Polymorphic behavior
shapes = [Rectangle(5, 4), Circle(3)]
for shape in shapes:
    print(shape.area())
```

### 4.4 Encapsulation
```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
    
    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())
```

## Conclusion
This guide covers essential Python intermediate topics, providing comprehensive examples and practical implementations across file handling, error management, modular programming, and object-oriented design.
