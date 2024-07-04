import sys
from pprint import pprint
import logging
from functools import partial

################################################################## 1. Using the print statement
print("Hello, World!")

################################################################## 2. Using Multiple Arguments with print
name = "Alice"
age = 30
print("Name:", name, "Age:", age)

################################################################## 3. Using str.format method
name = "Bob"
age = 25
print("Name: {}, Age: {}".format(name, age))

################################################################## 4. Using F-strings (Formatted String Literals)
name = "Charlie"
age = 35
print(f"Name: {name}, Age: {age}")

################################################################## 5. Using Concatenation
name = "David"
age = 40
print("Name: " + name + ", Age: " + str(age))

################################################################## 6. Printing Multiple Lines
print("Line 1\nLine 2\nLine 3")  # Using escape character \n
print("""Line 1
Line 2
Line 3""")  # Using triple quotes for multi-line strings

################################################################## 7. Printing with Different Separators
print("a", "b", "c", sep="-")  # Output: a-b-c

################################################################## 8. Printing to a File
with open("output.txt", "w") as f:
    print("Hello, File!", file=f)

################################################################## 9. Redirecting stdout to a File
with open("output.txt", "w") as f:
    original_stdout = sys.stdout
    sys.stdout = f
    print("Hello, File!")
    sys.stdout = original_stdout

################################################################## 10. Using sys.stdout.write
with open("output.txt", "w") as f:
    original_stdout = sys.stdout
    sys.stdout = f
    sys.stdout.write("Hello, World!\n")
    sys.stdout = original_stdout

################################################################## 11. Printing with end Parameter
print("Hello", end=", ")
print("World!")  # Output: Hello, World!

################################################################## 12. Using logging Module
logging.basicConfig(level=logging.INFO)
logging.info("Hello, World!")

################################################################## 13. Using print in a List Comprehension
[print(num) for num in range(5)]

################################################################## 14. Using print in a Generator Expression
gen = (num for num in range(5))
print(*gen)

################################################################## 15. Using pprint Module for Pretty Printing
data = {'name': 'Alice', 'age': 30}
pprint(data)

################################################################## 16. Printing to Standard Error (sys.stderr)
print("Error message", file=sys.stderr)

################################################################## 17. Using functools.partial to Create a Custom Print Function
custom_print = partial(print, end=' ')
custom_print("Hello,")
custom_print("World!")  # Output: Hello, World!

################################################################## 18. Using a Custom Logging Configuration
logging.basicConfig(filename='app.log', level=logging.DEBUG)
logging.debug('This is a debug message')    
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

################################################################## 19. Using format method with indices
name = "Eve"
age = 28
print("Name: {0}, Age: {1}".format(name, age))

################################################################## 20. Using format method with keyword arguments
print("Name: {name}, Age: {age}".format(name=name, age=age))

################################################################## 21. Using repr for detailed string representation
value = 42
print("The value is", repr(value))  # Output: The value is 42

################################################################## 22. Printing Unicode characters
print("Unicode test: \u2713 \u2714")  # Output: Unicode test: ✓ ✔

################################################################## 23. Using print with flush
print("This will be flushed immediately.", flush=True)

################################################################## 24. Using print with % formatting (old style)
name = "Frank"
age = 32
print("Name: %s, Age: %d" % (name, age))
