# Advanced Object-Oriented Programming in Python

## Table of Contents
1. Advanced Class Patterns
2. Metaclasses
3. Descriptors
4. Context Managers
5. Advanced Property Patterns
6. Multiple Inheritance Patterns
7. Advanced Design Patterns
8. Mixins and Traits
9. Advanced Magic Methods
10. Data Classes and Alternatives

## 1. Advanced Class Patterns

### 1.1 Class Decorators
```python
def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Database:
    def __init__(self):
        self.connection = "Connected"
    
    def query(self):
        return "Executing query..."

# Usage
db1 = Database()
db2 = Database()
print(db1 is db2)  # Output: True
```

### 1.2 Advanced Class Factory
```python
class ValidationMixin:
    def validate(self):
        return all(hasattr(self, attr) for attr in self.required_attrs)

def create_model(name, fields, bases=(object,)):
    def __init__(self, **kwargs):
        for field in fields:
            setattr(self, field, kwargs.get(field))
    
    cls_dict = {
        '__init__': __init__,
        'required_attrs': fields
    }
    
    return type(name, bases + (ValidationMixin,), cls_dict)

# Usage
UserModel = create_model('User', ['name', 'email', 'age'])
user = UserModel(name="John", email="john@example.com", age=30)
print(user.validate())  # Output: True
```

## 2. Metaclasses

### 2.1 Basic Metaclass
```python
class ValidatorMeta(type):
    def __new__(mcs, name, bases, namespace):
        # Add validation to all method calls
        for key, value in namespace.items():
            if callable(value) and not key.startswith('__'):
                namespace[key] = mcs.validate_call(value)
        return super().__new__(mcs, name, bases, namespace)
    
    @staticmethod
    def validate_call(func):
        def wrapper(*args, **kwargs):
            print(f"Validating call to {func.__name__}")
            return func(*args, **kwargs)
        return wrapper

class MyClass(metaclass=ValidatorMeta):
    def my_method(self):
        return "Method called"

# Usage
obj = MyClass()
print(obj.my_method())  # Will print validation message first
```

### 2.2 Registry Metaclass
```python
class RegisteredMeta(type):
    _registry = {}
    
    def __new__(mcs, name, bases, namespace):
        cls = super().__new__(mcs, name, bases, namespace)
        if bases:  # Don't register the base class
            mcs._registry[name] = cls
        return cls
    
    @classmethod
    def get_registry(mcs):
        return dict(mcs._registry)

class BasePlugin(metaclass=RegisteredMeta):
    pass

class Plugin1(BasePlugin):
    def run(self):
        return "Plugin 1 running"

class Plugin2(BasePlugin):
    def run(self):
        return "Plugin 2 running"

# Usage
plugins = RegisteredMeta.get_registry()
for name, plugin_cls in plugins.items():
    plugin = plugin_cls()
    print(f"{name}: {plugin.run()}")
```

## 3. Descriptors

### 3.1 Advanced Descriptor
```python
class ValidatedDescriptor:
    def __init__(self, minimum=None, maximum=None):
        self.minimum = minimum
        self.maximum = maximum
        self.name = None
    
    def __set_name__(self, owner, name):
        self.name = name
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)
    
    def __set__(self, instance, value):
        if self.minimum is not None and value < self.minimum:
            raise ValueError(f"{self.name} cannot be less than {self.minimum}")
        if self.maximum is not None and value > self.maximum:
            raise ValueError(f"{self.name} cannot be greater than {self.maximum}")
        instance.__dict__[self.name] = value

class Person:
    age = ValidatedDescriptor(minimum=0, maximum=150)
    height = ValidatedDescriptor(minimum=0, maximum=300)

# Usage
person = Person()
person.age = 25  # OK
try:
    person.age = -1  # Raises ValueError
except ValueError as e:
    print(e)
```

## 4. Advanced Property Patterns

### 4.1 Computed Properties
```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
        self._area = None
        self._circumference = None
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        self._radius = value
        # Invalidate cached computations
        self._area = None
        self._circumference = None
    
    @property
    def area(self):
        if self._area is None:
            import math
            self._area = math.pi * self._radius ** 2
        return self._area
    
    @property
    def circumference(self):
        if self._circumference is None:
            import math
            self._circumference = 2 * math.pi * self._radius
        return self._circumference

# Usage
circle = Circle(5)
print(circle.area)  # Computed only once
print(circle.area)  # Returns cached value
circle.radius = 6   # Invalidates cache
print(circle.area)  # Recomputed
```

## 5. Advanced Multiple Inheritance

### 5.1 Diamond Problem Resolution
```python
class Base:
    def method(self):
        print("Base.method() called")

class A(Base):
    def method(self):
        super().method()
        print("A.method() called")

class B(Base):
    def method(self):
        super().method()
        print("B.method() called")

class C(A, B):
    def method(self):
        super().method()
        print("C.method() called")

# Usage
c = C()
c.method()
print(C.__mro__)  # View method resolution order
```

### 5.2 Mixin Classes
```python
class SerializeMixin:
    def to_dict(self):
        return {
            key: value 
            for key, value in self.__dict__.items() 
            if not key.startswith('_')
        }
    
    def to_json(self):
        import json
        return json.dumps(self.to_dict())

class LoggerMixin:
    def log(self, message):
        print(f"{self.__class__.__name__}: {message}")

class User(SerializeMixin, LoggerMixin):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.log(f"Created user {name}")

# Usage
user = User("John", "john@example.com")
print(user.to_json())
```

## 6. Advanced Design Patterns

### 6.1 Observer Pattern
```python
class Observable:
    def __init__(self):
        self._observers = []
        self._state = None
    
    def attach(self, observer):
        self._observers.append(observer)
    
    def detach(self, observer):
        self._observers.remove(observer)
    
    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self, value):
        self._state = value
        self._notify_observers()
    
    def _notify_observers(self):
        for observer in self._observers:
            observer.update(self._state)

class Observer:
    def __init__(self, name):
        self.name = name
    
    def update(self, state):
        print(f"{self.name} received update: {state}")

# Usage
subject = Observable()
observer1 = Observer("Observer 1")
observer2 = Observer("Observer 2")

subject.attach(observer1)
subject.attach(observer2)
subject.state = "New State"
```

### 6.2 Command Pattern
```python
from abc import ABC, abstractmethod
from typing import Dict, List

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass
    
    @abstractmethod
    def undo(self):
        pass

class TextEditor:
    def __init__(self):
        self.text = ""
    
    def insert(self, text):
        self.text += text
    
    def delete(self, length):
        if length <= len(self.text):
            self.text = self.text[:-length]
    
    def get_text(self):
        return self.text

class InsertCommand(Command):
    def __init__(self, editor: TextEditor, text: str):
        self.editor = editor
        self.text = text
    
    def execute(self):
        self.editor.insert(self.text)
    
    def undo(self):
        self.editor.delete(len(self.text))

class CommandInvoker:
    def __init__(self):
        self._commands: List[Command] = []
        self._current = -1
    
    def execute(self, command: Command):
        self._current += 1
        if self._current < len(self._commands):
            self._commands[self._current:] = []
        self._commands.append(command)
        command.execute()
    
    def undo(self):
        if self._current >= 0:
            self._commands[self._current].undo()
            self._current -= 1
    
    def redo(self):
        if self._current + 1 < len(self._commands):
            self._current += 1
            self._commands[self._current].execute()

# Usage
editor = TextEditor()
invoker = CommandInvoker()

invoker.execute(InsertCommand(editor, "Hello "))
invoker.execute(InsertCommand(editor, "World!"))
print(editor.get_text())  # Output: Hello World!
invoker.undo()
print(editor.get_text())  # Output: Hello
invoker.redo()
print(editor.get_text())  # Output: Hello World!
```

## 7. Advanced Magic Methods

### 7.1 Custom Container
```python
class DataList:
    def __init__(self, *items):
        self._items = list(items)
    
    def __getitem__(self, index):
        return self._items[index]
    
    def __setitem__(self, index, value):
        self._items[index] = value
    
    def __len__(self):
        return len(self._items)
    
    def __iter__(self):
        return iter(self._items)
    
    def __contains__(self, item):
        return item in self._items
    
    def __add__(self, other):
        if isinstance(other, DataList):
            return DataList(*(self._items + other._items))
        return NotImplemented
    
    def __call__(self):
        return sum(self._items)
    
    def __str__(self):
        return f"DataList({self._items})"

# Usage
data = DataList(1, 2, 3, 4, 5)
print(len(data))        # Output: 5
print(3 in data)        # Output: True
print(data[1])         # Output: 2
print(data())          # Output: 15
```

### 7.2 Context Manager Implementation
```python
class Transaction:
    def __init__(self, database):
        self.db = database
        self.transaction_level = 0
    
    def __enter__(self):
        self.transaction_level += 1
        if self.transaction_level == 1:
            self.db.begin_transaction()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.transaction_level -= 1
        if self.transaction_level == 0:
            if exc_type is None:
                self.db.commit()
            else:
                self.db.rollback()
        return False  # Don't suppress exceptions

class Database:
    def begin_transaction(self):
        print("Beginning transaction")
    
    def commit(self):
        print("Committing transaction")
    
    def rollback(self):
        print("Rolling back transaction")

# Usage
db = Database()
with Transaction(db):
    # Do something
    print("Working in transaction")
```

## 8. Data Classes and Alternatives

### 8.1 Advanced Data Classes
```python
from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Product:
    name: str
    price: float
    quantity: int = 0
    tags: List[str] = field(default_factory=list)
    description: Optional[str] = None
    
    def __post_init__(self):
        if self.price < 0:
            raise ValueError("Price cannot be negative")
    
    @property
    def total_value(self) -> float:
        return self.price * self.quantity
    
    def add_tag(self, tag: str) -> None:
        if tag not in self.tags:
            self.tags.append(tag)

# Usage
product = Product("Laptop", 999.99, 5, ["electronics", "computers"])
print(product.total_value)  # Output: 4999.95
product.add_tag("portable")
print(product.tags)  # Output: ['electronics', 'computers', 'portable']
```

### 8.2 Named Tuples with Inheritance
```python
from typing import NamedTuple

class Point(NamedTuple):
    x: float
    y: float
    
    def distance_from_origin(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

class Point3D(NamedTuple):
    x: float
    y: float
    z: float
    
    def distance_from_origin(self) -> float:
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

# Usage
p2d = Point(3, 4)
p3d = Point3D(3, 4, 5)
print(p2d.distance_from_origin())  # Output: 5.0
print(p3d.distance_from_origin())  # Output: 7.0710678118654755
```

## 9. Advanced Attribute Access

### 9.1 Custom Attribute Access
```python
class DynamicAttributes:
    def __init__(self, **kwargs):
        self._data = {}
        for key, value in kwargs.items():
            self._data[key] = value
    
    def __getattr__(self, name):
        if name in self._data:
            return self._data[name]
        raise AttributeError(f"'{self.__class__.__name__}' has no attribute '{name}'")
    
    def __setattr__(self, name, value):
        if name == '_data':
            super().__setattr__(name, value)
        else:
            self._data[name] = value
    
    def __delattr__(self, name):
        if name in self._data:
            del self._data[name]
        else:
            raise AttributeError(f"
