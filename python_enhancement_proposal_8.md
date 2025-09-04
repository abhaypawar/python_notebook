PEP 1 explains what PEPs are and how they work.

PEP 8 was written by Guido van Rossum (Python’s creator) and others, and became the canonical style guide.

Other famous PEPs:

PEP 20 → The Zen of Python (import this)

PEP 484 → Type hints

PEP 572 → The walrus operator (:=)

---

# 🐍 Python Coding Standards & PEP 8 Cheat Sheet (2025 Edition)

A practical, modern guide to **writing clean, professional Python code**.  
Covers **PEP 8**, industry standards (2025), and **rare pitfalls** every dev should know.

---

## 📌 1. Indentation & Line Length
- Use **4 spaces per indentation level** (never tabs).  
- Max line length: **88 chars** (modern consensus, e.g., `black` formatter).  

```python
def my_function():
    for i in range(5):
        print(i)  # ✅ Clean indentation
````

---

## 📌 2. Blank Lines

* 2 blank lines before **top-level functions/classes**.
* 1 blank line between methods in a class.

```python
class MyClass:
    def method_one(self):
        pass

    def method_two(self):
        pass
```

---

## 📌 3. Imports

* One import per line.
* Order: **standard library → third-party → local**.
* Use **absolute imports**, relative only inside packages.
* Avoid wildcard imports.

```python
import os
import sys

import requests

from myproject import utils
```

---

## 📌 4. Naming Conventions

* **Variables / functions** → `lower_case_with_underscores`
* **Classes** → `CapWords`
* **Constants** → `UPPER_CASE_WITH_UNDERSCORES`
* **Private/internal** → `_leading_underscore`

```python
MAX_SIZE = 100

def calculate_area(radius):
    return 3.14 * radius * radius

class Circle:
    def __init__(self, radius):
        self._radius = radius
```

---

## 📌 5. Spacing Rules

✅ Correct vs ❌ Wrong

```python
x = y + z        # ✅
x=y+z            # ❌

func(a, b, c)    # ✅
func(a , b , c ) # ❌

my_list = [1, 2, 3]  # ✅
my_list = [ 1 ,2 , 3 ]  # ❌
```

---

## 📌 6. Docstrings & Comments

* Use `"""triple quotes"""` for docstrings.
* First line = short summary.
* Comments explain **why**, not what.

```python
def add(x: int, y: int) -> int:
    """Return the sum of x and y."""
    return x + y
```

---

## 📌 7. Function & Class Definitions

* Break long arg lists after `(`.

```python
def my_function(param1, param2,
                param3, param4):
    pass
```

---

## 📌 8. Boolean Checks

* Don’t compare to `True` / `False`.

```python
if my_list:          # ✅
if len(my_list) != 0: # ✅
if my_list == True:  # ❌
```

---

## 📌 9. Whitespace Pitfalls

```python
if x == 4: print(x, y)  # ✅
if x == 4 : print(x , y )  # ❌
```

---

## 📌 10. General Principles

* **Readability > Cleverness**.
* Consistency matters.
* Follow *The Zen of Python* (`import this`).

---

## 📌 11. Code Layout

* Don’t align variables artificially.

```python
x = 1
y = 2
long_variable_name = 3  # ✅
```

---

## 📌 12. String Quotes

* Choose `'single'` or `"double"` consistently.
* Use `"""triple"""` for docstrings.

---

## 📌 13. Expressions & Statements

* Don’t use unnecessary parentheses.
* No semicolons.
* No multiple statements per line.

```python
if x and y:  # ✅
if (x and y):  # ❌
```

---

## 📌 14. Trailing Commas

```python
my_list = [
    1,
    2,
    3,
]
```

---

## 📌 15. Comparisons

* Use `is` for `None`, `==` for values.

```python
if foo is None:  # ✅
if foo == None:  # ❌
```

---

## 📌 16. Programming Recommendations

* Use `is not` instead of `not ... is`.
* Use `.startswith()` / `.endswith()`.
* Prefer `in` for membership.

```python
if name.startswith("Mr."):  # ✅
```

---

## 📌 17. Type Hints (Modern Standard)

* Always use **type hints** in new code.

```python
def greet(name: str) -> str:
    return f"Hello {name}"
```

---

## 📌 18. Variable Annotations

```python
count: int = 0
```

---

## 📌 19. f-Strings (2025 Standard)

* Use f-strings, not `format()` or `%`.

```python
name = "Alice"
print(f"Hello {name}!")  # ✅
```

---

## 📌 20. Path Handling

* Prefer `pathlib` over `os.path`.

```python
from pathlib import Path

data_dir = Path("data")
print(data_dir.exists())
```

---

## 📌 21. Loops

* Prefer `enumerate()` and `zip()` to manual indexing.

```python
for i, value in enumerate(my_list):
    print(i, value)
```

---

## 📌 22. Context Managers

* Always use `with` for file/connection handling.

```python
with open("file.txt") as f:
    data = f.read()
```

---

## 📌 23. Dataclasses (Modern Standard)

* Prefer `@dataclass` for simple data holders.

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int
```

---

## 📌 24. Tools & Linters

* Use **`black`** for formatting.
* Use **`ruff` or `flake8`** for linting.
* Use **`mypy`** for type checking.

---

## 📌 25. Rare Pitfalls & Gotchas

⚠️ These cause **real-world bugs** if ignored:

* **Mutable default args**:

  ```python
  def bad(x, items=[]):   # ❌ Dangerous!
      items.append(x)
      return items

  def good(x, items=None):  # ✅
      if items is None:
          items = []
      items.append(x)
      return items
  ```

* **Late binding closures**:

  ```python
  funcs = [lambda: i for i in range(3)]
  print([f() for f in funcs])  # ❌ [2, 2, 2]

  funcs = [lambda i=i: i for i in range(3)]
  print([f() for f in funcs])  # ✅ [0, 1, 2]
  ```

* **Floating-point precision**:

  ```python
  0.1 + 0.2 == 0.3  # ❌ False
  ```

* **Chained mutable defaults** (dict/set pitfalls).

---

## 📌 26. When in Doubt

* Be consistent with the existing project.
* Prioritize readability.
* Automate checks with **pre-commit hooks**.

---

# ✅ Final Thoughts

PEP 8 isn’t about perfection — it’s about **consistency, clarity, and collaboration**.
In 2025, teams standardize with:

* **black** (formatting)
* **ruff/flake8** (linting)
* **mypy** (type safety)

Write Python that’s:

* **Readable**
* **Predictable**
* **Maintainable**

---

# 🐍 Python PEPs Made Simple (2025 Edition)

PEP = **Python Enhancement Proposal**.  
It’s like a “rulebook page” or “proposal” for Python

Some PEPs are **rules for writing code (style)**.  
Some are **new features**.  
Some are **about packaging/distribution**.  

This doc explains the **most useful PEPs** simply, with examples.  

---

# 📌 PEP 8 – Style Guide for Python Code
The **grammar rules** for Python code.  

✅ Example:
```python
def add(x: int, y: int) -> int:
    return x + y
````

❌ Example:

```python
def add(x,y):return x+y
```

Main ideas:

* 4 spaces for indentation.
* Max \~88 chars per line.
* Clear names (`total_price` not `tp`).
* Add spaces around operators (`x = y + z`).

---

# 📌 PEP 20 – The Zen of Python

Python’s **philosophy**. See it by typing:

```python
import this
```

Key rules:

* **Explicit is better than implicit** → Be clear.
* **Simple is better than complex** → Don’t overcomplicate.
* **Readability counts** → Code should be easy to read.

---

# 📌 PEP 257 – Docstring Conventions

How to write docstrings (function/class comments).

✅ Example:

```python
def greet(name: str) -> str:
    """Return a greeting message for the given name."""
    return f"Hello {name}"
```

---

# 📌 PEP 234 – Iterators

Introduced the **iterator protocol** → made `for` loops powerful.

```python
for letter in "hello":
    print(letter)
```

---

# 📌 PEP 343 – The `with` Statement

Introduced **context managers**.
Automatically handles closing files, connections, etc.

✅ Example:

```python
with open("file.txt") as f:
    data = f.read()
```

❌ Example:

```python
f = open("file.txt")
data = f.read()
f.close()  # you must remember this
```

---

# 📌 PEP 484 – Type Hints

Added **type hints** → makes code easier to read and check.

```python
def add(x: int, y: int) -> int:
    return x + y
```

---

# 📌 PEP 526 – Variable Annotations

Lets you add type hints to variables.

```python
count: int = 0
```

---

# 📌 PEP 572 – Assignment Expressions (`:=`)

Introduced the **walrus operator**. Assign a value inside an expression.

✅ Example:

```python
while (line := input("Type: ")) != "quit":
    print(line)
```

---

# 📌 PEP 585 – Built-in Generics

Use built-in types directly for typing.

✅ Example:

```python
def get_numbers() -> list[int]:
    return [1, 2, 3]
```

❌ Old way:

```python
from typing import List
def get_numbers() -> List[int]:
    return [1, 2, 3]
```

---

# 📌 PEP 604 – Union Types

Simpler syntax for multiple possible types.

✅ Example:

```python
def square(x: int | float) -> float:
    return x * x
```

❌ Old way:

```python
from typing import Union
def square(x: Union[int, float]) -> float:
    return x * x
```

---

# 📌 PEP 563 & PEP 649 – Type Annotations Future

* **PEP 563** (postponed evaluation) → annotations were stored as strings.
* **PEP 649** → newer solution, keeps them efficient without breaking tools.

Result: type hints are **fast and memory-friendly** in new Python versions.

---

# 📌 PEP 572 – Walrus Operator

Lets you assign inside conditions.

```python
if (n := len([1, 2, 3])) > 2:
    print(f"List has {n} items")
```

---

# 📌 PEP 618 – Extended `zip()`

Adds `strict=True` option. Raises error if zipped lists aren’t same length.

```python
zip([1, 2], [3], strict=True)  # ❌ Error
```

---

# 📌 PEP 622 – Pattern Matching (Structural)

Introduced `match` / `case` (Python 3.10).
Like `switch` in other languages, but more powerful.

✅ Example:

```python
def handle(value):
    match value:
        case 0:
            return "zero"
        case [x, y]:
            return f"pair: {x}, {y}"
        case _:
            return "something else"
```

---

# 📌 PEP 654 – Exception Groups

Handle multiple errors together.

```python
try:
    ...
except* ValueError as e:
    print("value error")
```

---

# 📌 PEP 701 – f-strings Everywhere

You can now use **f-strings inside more places**, like docstrings.

---

# 📌 Packaging PEPs

These affect how Python projects are shared and installed:

* **PEP 427 – Wheels** → `.whl` files = faster installs.
* **PEP 440 – Versioning** → standard rules for versions (`1.0.0`, `2.1.3b1`).
* **PEP 518 – `pyproject.toml`** → modern project config.
* **PEP 621 – Metadata in TOML** → standard way to write project info.

Example `pyproject.toml`:

```toml
[project]
name = "myapp"
version = "1.0.0"
dependencies = ["requests"]
```

---

# 📌 Rare But Important PEPs

* **PEP 572 – Walrus Operator** (again, because it’s easy to misuse).
* **PEP 622 – Pattern Matching** can be tricky:

  * Order matters (like if/elif).
  * `_` means “anything”.

---

# ✅ Summary Table

| PEP | What it does         | Why it matters                         |                        |
| --- | -------------------- | -------------------------------------- | ---------------------- |
| 8   | Style guide          | Code looks clean & consistent          |                        |
| 20  | Zen of Python        | Philosophy: keep it simple, readable   |                        |
| 257 | Docstrings           | Standard way to explain code           |                        |
| 234 | Iterators            | Makes `for` loops powerful             |                        |
| 343 | `with`               | Auto-close files/resources             |                        |
| 484 | Type hints           | Easier to read/check functions         |                        |
| 526 | Variable annotations | Type hints for variables               |                        |
| 572 | Walrus operator      | Assign inside expressions              |                        |
| 585 | Built-in generics    | Use `list[int]` instead of `List[int]` |                        |
| 604 | Union types          | Use \`int                              | str`instead of`Union\` |
| 622 | Match/case           | Pattern matching (Python 3.10)         |                        |
| 654 | Exception groups     | Handle multiple errors                 |                        |
| 427 | Wheel format         | Faster package installs                |                        |
| 518 | pyproject.toml       | Standard project config                |                        |
| 621 | Metadata in TOML     | Project info in one place              |                        |

---

# 🚀 Final Thoughts

* **PEP 8 + PEP 20** = how to write and think in Python.
* **Type hints (PEP 484, 585, 604)** = modern standard (2025).
* **Packaging PEPs (518, 621)** = all new projects should use `pyproject.toml`.
* **Pattern matching (PEP 622)** = powerful but use carefully.
* **Linters + formatters** (black, ruff, mypy) → enforce these rules automatically.

Python keeps evolving, but these PEPs are the ones you’ll use every day.

```

