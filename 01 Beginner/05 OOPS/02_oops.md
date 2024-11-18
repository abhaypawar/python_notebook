# Complete Guide to Object-Oriented Programming in Python

## Table of Contents
1. Basic Class Concepts
2. Constructor and Instance Methods
3. Class Variables vs Instance Variables
4. Inheritance and Multiple Inheritance
5. Polymorphism
6. Encapsulation and Access Modifiers
7. Abstraction and Interfaces
8. Class Methods and Static Methods
9. Property Decorators
10. Magic Methods
11. Composition vs Inheritance
12. Real-world Applications

## 1. Basic Class Concepts

### Creating Your First Class
```python
class Dog:
    # Class variable (shared by all instances)
    species = "Canis familiaris"
    
    # Constructor method
    def __init__(self, name, age):
        # Instance variables (unique to each instance)
        self.name = name
        self.age = age
    
    # Instance method
    def bark(self):
        return f"{self.name} says Woof!"

# Creating instances
buddy = Dog("Buddy", 5)
max = Dog("Max", 3)

print(buddy.bark())  # Output: Buddy says Woof!
print(max.species)   # Output: Canis familiaris
```

## 2. Constructor and Different Types of Methods

```python
class BankAccount:
    # Class variable
    bank_name = "MyBank"
    
    def __init__(self, account_holder, initial_balance=0):
        self.holder = account_holder
        self.balance = initial_balance
        self._account_number = self._generate_account_number()
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        return "Invalid amount"
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrawn ${amount}. New balance: ${self.balance}"
        return "Insufficient funds"
    
    @property
    def account_info(self):
        return f"Account holder: {self.holder}, Balance: ${self.balance}"
    
    @staticmethod
    def _generate_account_number():
        import random
        return random.randint(10000, 99999)

# Usage
account = BankAccount("John Doe", 1000)
print(account.deposit(500))    # Output: Deposited $500. New balance: $1500
print(account.account_info)    # Output: Account holder: John Doe, Balance: $1500
```

## 3. Inheritance and Multiple Inheritance

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

class Flyable:
    def fly(self):
        return f"{self.name} is flying!"

class Bird(Animal, Flyable):
    def speak(self):
        return f"{self.name} chirps!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} meows!"

# Usage
parrot = Bird("Rio")
kitty = Cat("Whiskers")

print(parrot.speak())  # Output: Rio chirps!
print(parrot.fly())    # Output: Rio is flying!
print(kitty.speak())   # Output: Whiskers meows!
```

## 4. Encapsulation with Property Decorators

```python
class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary
    
    @property
    def name(self):
        return self._name
    
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = value
    
    @salary.deleter
    def salary(self):
        self._salary = 0

# Usage
emp = Employee("Alice", 50000)
print(emp.salary)      # Output: 50000
emp.salary = 60000     # Using setter
print(emp.salary)      # Output: 60000
del emp.salary         # Using deleter
print(emp.salary)      # Output: 0
```

## 5. Abstract Classes and Interfaces

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        import math
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        import math
        return 2 * math.pi * self.radius

# Usage
rect = Rectangle(5, 3)
circle = Circle(4)

print(f"Rectangle area: {rect.area()}")        # Output: Rectangle area: 15
print(f"Circle perimeter: {circle.perimeter()}")  # Output: Circle perimeter: 25.132741228718345
```

## 6. Composition Example

```python
class Engine:
    def __init__(self, power):
        self.power = power
    
    def start(self):
        return "Engine started"

class Wheels:
    def __init__(self, count):
        self.count = count
    
    def rotate(self):
        return f"{self.count} wheels rotating"

class Car:
    def __init__(self, model, engine_power, wheel_count):
        self.model = model
        self.engine = Engine(engine_power)  # Composition
        self.wheels = Wheels(wheel_count)   # Composition
    
    def start_drive(self):
        return f"{self.model}: {self.engine.start()} and {self.wheels.rotate()}"

# Usage
my_car = Car("Tesla", 300, 4)
print(my_car.start_drive())  
# Output: Tesla: Engine started and 4 wheels rotating
```

## 7. Magic Methods (Dunder Methods)

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __len__(self):
        import math
        return int(math.sqrt(self.x**2 + self.y**2))

# Usage
p1 = Point(2, 3)
p2 = Point(3, 4)

print(p1)           # Output: Point(2, 3)
print(p1 + p2)      # Output: Point(5, 7)
print(p1 == p2)     # Output: False
print(len(p1))      # Output: 3
```

## 8. Real-world Application: Simple Library System

```python
from datetime import datetime, timedelta

class LibraryItem:
    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id
        self.checked_out = False
        self.due_date = None

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            self.due_date = datetime.now() + timedelta(days=14)
            return True
        return False

    def return_item(self):
        self.checked_out = False
        self.due_date = None

class Book(LibraryItem):
    def __init__(self, title, item_id, author, pages):
        super().__init__(title, item_id)
        self.author = author
        self.pages = pages

class DVD(LibraryItem):
    def __init__(self, title, item_id, director, duration):
        super().__init__(title, item_id)
        self.director = director
        self.duration = duration

class Library:
    def __init__(self):
        self.items = {}
        self.members = {}

    def add_item(self, item):
        self.items[item.item_id] = item

    def check_out_item(self, item_id, member_id):
        if item_id in self.items and member_id in self.members:
            item = self.items[item_id]
            if item.check_out():
                return f"{item.title} has been checked out. Due date: {item.due_date}"
            return "Item is already checked out"
        return "Invalid item or member ID"

# Usage Example
library = Library()

# Adding items to library
book = Book("The Python Way", "B001", "John Smith", 300)
dvd = DVD("Python Programming", "D001", "Jane Doe", 120)

library.add_item(book)
library.add_item(dvd)

# Adding a member
library.members["M001"] = {"name": "Alice Johnson"}

# Checking out items
print(library.check_out_item("B001", "M001"))
# Output: The Python Way has been checked out. Due date: [future date]
```

## Best Practices and Tips

1. Always use clear, descriptive names for classes and methods
2. Follow the Single Responsibility Principle
3. Use inheritance when there is a clear "is-a" relationship
4. Prefer composition over inheritance for complex relationships
5. Use abstract classes to define interfaces
6. Keep your classes focused and cohesive
7. Use proper encapsulation to protect data
8. Document your classes and methods
9. Use type hints for better code clarity
10. Write unit tests for your classes

## Common Patterns in Python OOP

1. Singleton Pattern
```python
class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# Usage
s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # Output: True
```

2. Factory Pattern
```python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type.lower() == "dog":
            return Dog()
        elif animal_type.lower() == "cat":
            return Cat()
        raise ValueError("Invalid animal type")

# Usage
factory = AnimalFactory()
dog = factory.create_animal("dog")
cat = factory.create_animal("cat")

print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!
```
