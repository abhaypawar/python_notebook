# Comprehensive Guide to Python Methods and Decorators

## Table of Contents
1. Instance Methods
2. Class Methods
3. Static Methods
4. Property Methods
5. Custom Decorators
6. Built-in Decorators
7. Method Decorators
8. Property Variations
9. Advanced Decorator Patterns
10. Real-world Applications

## 1. Instance Methods vs Other Methods

```python
class Employee:
    company = "TechCorp"
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    # Instance method - has access to instance attributes via self
    def get_salary(self):
        return f"{self.name}'s salary is ${self.salary}"
    
    # Class method - has access to class attributes via cls
    @classmethod
    def get_company(cls):
        return f"Company name is {cls.company}"
    
    # Static method - no access to instance or class attributes
    @staticmethod
    def is_workday(day):
        return day.weekday() < 5

# Usage
emp = Employee("John", 50000)
print(emp.get_salary())      # Instance method
print(Employee.get_company()) # Class method

import datetime
date = datetime.date(2024, 1, 1)
print(Employee.is_workday(date)) # Static method
```

## 2. Class Methods In-Depth

### 2.1 Alternative Constructors
```python
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    
    @classmethod
    def from_string(cls, date_string):
        year, month, day = map(int, date_string.split('-'))
        return cls(year, month, day)
    
    @classmethod
    def from_timestamp(cls, timestamp):
        import datetime
        date = datetime.datetime.fromtimestamp(timestamp)
        return cls(date.year, date.month, date.day)
    
    def __str__(self):
        return f"{self.year}-{self.month:02d}-{self.day:02d}"

# Usage
date1 = Date.from_string("2024-01-15")
date2 = Date.from_timestamp(1704067200)  # 2024-01-01
print(date1)  # Output: 2024-01-15
print(date2)  # Output: 2024-01-01
```

### 2.2 Factory Methods
```python
class DatabaseConnection:
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password
    
    @classmethod
    def development(cls):
        return cls("localhost", "dev_user", "dev_password")
    
    @classmethod
    def production(cls):
        return cls("prod.server.com", "prod_user", "prod_password")
    
    @classmethod
    def testing(cls):
        return cls("test.server.com", "test_user", "test_password")

# Usage
dev_db = DatabaseConnection.development()
prod_db = DatabaseConnection.production()
```

## 3. Static Methods In-Depth

### 3.1 Utility Functions
```python
class MathOperations:
    @staticmethod
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    @staticmethod
    def factorial(n):
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        if n == 0:
            return 1
        return n * MathOperations.factorial(n - 1)
    
    @staticmethod
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

# Usage
print(MathOperations.is_prime(17))    # True
print(MathOperations.factorial(5))     # 120
print(MathOperations.gcd(48, 18))      # 6
```

## 4. Property Methods In-Depth

### 4.1 Basic Property Usage
```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        """Get the circle's radius"""
        return self._radius
    
    @radius.setter
    def radius(self, value):
        """Set the circle's radius"""
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value
    
    @property
    def area(self):
        """Calculate the circle's area"""
        import math
        return math.pi * self._radius ** 2
    
    @property
    def circumference(self):
        """Calculate the circle's circumference"""
        import math
        return 2 * math.pi * self._radius

# Usage
circle = Circle(5)
print(circle.radius)         # Using getter
circle.radius = 10           # Using setter
print(circle.area)          # Computed property
print(circle.circumference) # Computed property
```

### 4.2 Advanced Property Patterns
```python
class Temperature:
    def __init__(self):
        self._celsius = 0
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        self._celsius = value
    
    @property
    def fahrenheit(self):
        return (self.celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5/9
    
    @property
    def kelvin(self):
        return self.celsius + 273.15
    
    @kelvin.setter
    def kelvin(self, value):
        self.celsius = value - 273.15

# Usage
temp = Temperature()
temp.celsius = 25
print(temp.fahrenheit)  # 77.0
temp.fahrenheit = 68
print(temp.celsius)     # 20.0
print(temp.kelvin)      # 293.15
```

## 5. Custom Decorators

### 5.1 Basic Function Decorators
```python
def timer(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.2f} seconds to execute")
        return result
    return wrapper

def memoize(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

# Usage
@timer
@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(35))
```

### 5.2 Class Decorators with Parameters
```python
def validate_types(**expected_types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Validate positional arguments
            for arg, expected_type in zip(args[1:], expected_types.values()):
                if not isinstance(arg, expected_type):
                    raise TypeError(f"Expected {expected_type}, got {type(arg)}")
            
            # Validate keyword arguments
            for arg_name, arg_value in kwargs.items():
                if arg_name in expected_types:
                    expected_type = expected_types[arg_name]
                    if not isinstance(arg_value, expected_type):
                        raise TypeError(f"Expected {expected_type} for {arg_name}, got {type(arg_value)}")
            
            return func(*args, **kwargs)
        return wrapper
    return decorator

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @validate_types(name=str, age=int)
    def update_info(self, name, age):
        self.name = name
        self.age = age

# Usage
person = Person("John", 30)
person.update_info("Jane", 25)  # Works
try:
    person.update_info("Jane", "25")  # Raises TypeError
except TypeError as e:
    print(e)
```

## 6. Property Variations

### 6.1 Cached Properties
```python
class cached_property:
    def __init__(self, func):
        self.func = func
        self.name = func.__name__
    
    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        
        value = self.func(instance)
        setattr(instance, self.name, value)
        return value

class ExpensiveComputation:
    def __init__(self, data):
        self.data = data
    
    @cached_property
    def processed_data(self):
        print("Processing data...")
        import time
        time.sleep(1)  # Simulate expensive computation
        return [x * 2 for x in self.data]

# Usage
comp = ExpensiveComputation([1, 2, 3, 4, 5])
print(comp.processed_data)  # Computes and caches
print(comp.processed_data)  # Returns cached value
```

## 7. Method Chaining Decorators

```python
class ChainableMethods:
    def __init__(self, value):
        self.value = value
    
    def chainable(func):
        def wrapper(self, *args, **kwargs):
            func(self, *args, **kwargs)
            return self
        return wrapper
    
    @chainable
    def add(self, x):
        self.value += x
    
    @chainable
    def multiply(self, x):
        self.value *= x
    
    @chainable
    def power(self, x):
        self.value **= x
    
    def get_result(self):
        return self.value

# Usage
result = ChainableMethods(2)\
    .add(3)\
    .multiply(4)\
    .power(2)\
    .get_result()
print(result)  # ((2 + 3) * 4)^2 = 400
```

## 8. Context Manager Decorators

```python
from contextlib import contextmanager

class Resource:
    @contextmanager
    def resource_manager(self):
        print("Acquiring resource")
        try:
            yield self
        finally:
            print("Releasing resource")
    
    def process(self):
        print("Processing with resource")

# Usage
resource = Resource()
with resource.resource_manager():
    resource.process()
```

## 9. Advanced Decorator Patterns

### 9.1 Decorator with State
```python
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Call count for {self.func.__name__}: {self.count}")
        return self.func(*args, **kwargs)
    
    def reset_count(self):
        self.count = 0

@CountCalls
def my_function():
    return "Function called"

# Usage
my_function()  # Call count: 1
my_function()  # Call count: 2
my_function.reset_count()
my_function()  # Call count: 1
```

### 9.2 Parametrized Class Decorator
```python
def singleton(thread_safe=False):
    def decorator(cls):
        instances = {}
        
        if thread_safe:
            import threading
            lock = threading.Lock()
        
        def get_instance(*args, **kwargs):
            if thread_safe:
                with lock:
                    if cls not in instances:
                        instances[cls] = cls(*args, **kwargs)
            else:
                if cls not in instances:
                    instances[cls] = cls(*args, **kwargs)
            return instances[cls]
        
        return get_instance
    
    return decorator

@singleton(thread_safe=True)
class DatabaseConnection:
    def __init__(self):
        print("Initializing database connection")

# Usage
db1 = DatabaseConnection()
db2 = DatabaseConnection()  # Returns same instance
print(db1 is db2)  # True
```

## 10. Real-world Application Example

```python
class APIEndpoint:
    def __init__(self, base_url):
        self.base_url = base_url
        self._cache = {}
    
    def cache_result(func):
        def wrapper(self, *args, **kwargs):
            cache_key = (func.__name__, args, tuple(kwargs.items()))
            if cache_key in self._cache:
                print("Returning cached result")
                return self._cache[cache_key]
            
            result = func(self, *args, **kwargs)
            self._cache[cache_key] = result
            return result
        return wrapper
    
    def validate_params(required_params):
        def decorator(func):
            def wrapper(self, *args, **kwargs):
                for param in required_params:
                    if param not in kwargs:
                        raise ValueError(f"Missing required parameter: {param}")
                return func(self, *args, **kwargs)
            return wrapper
        return decorator
    
    @cache_result
    @validate_params(['user_id'])
    def get_user(self, **params):
        # Simulate API call
        user_id = params['user_id']
        return {"id": user_id, "name": f"User {user_id}"}
    
    @property
    def cache_size(self):
        return len(self._cache)
    
    @classmethod
    def create_development(cls):
        return cls("http://api.dev.example.com")
    
    @classmethod
    def create_production(cls):
        return cls("http://api.example.com")

# Usage
api = APIEndpoint.create_development()

# First call - makes "API call"
user = api.get_user(user_id=123)
print(user)

# Second call - returns cached result
same_user = api.get_user(user_id=123)
print(same_user)

# Missing required parameter
try:
    api.get_user()  # Raises ValueError
except ValueError as e:
    print(e)

print(f"Cache size: {api.cache_size}")
```

## Best Practices and Tips

1. Use `@classmethod` for alternative constructors
2. Use `@staticmethod` for utility functions that don't need access to instance/class
3. Use `@property` for computed attributes and validation
4. Keep decorators focused and single-purpose
5. Use method chaining when it improves readability
6. Cache expensive computations when appropriate
7. Use type hints with decorators for better IDE support
8. Document decorator behavior clearly
9. Consider using `functools.wraps` to preserve function metadata
10. Test decorated methods thoroughly
