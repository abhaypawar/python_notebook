########################################################################################################################   Integers 
num1 = 10
num2 = -5

########################################################################################################################   Arithmetic operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
exponentiation = num1 ** 2
floor_division = num1 // num2
modulus = num1 % num2

print(":::::::::::::::::Integers:::::::::::::::::::::")
print("Addition:", addition)  # Output: 5
print("Subtraction:", subtraction)  # Output: 15
print("Multiplication:", multiplication)  # Output: -50
print("Division:", division)  # Output: -2.0
print("Exponentiation:", exponentiation)  # Output: 100
print("Floor Division:", floor_division)  # Output: -2
print("Modulus:", modulus)  # Output: 0

########################################################################################################################   Floating-point numbers 
float1 = 3.14
float2 = -2.5

# Arithmetic operations
addition_float = float1 + float2
subtraction_float = float1 - float2
multiplication_float = float1 * float2
division_float = float1 / float2
exponentiation_float = float1 ** 2

print("\n:::::::::::::::::Floating-point numbers:::::::::::::::::::::")
print("Addition:", addition_float)  # Output: 0.64
print("Subtraction:", subtraction_float)  # Output: 5.64
print("Multiplication:", multiplication_float)  # Output: -7.85
print("Division:", division_float)  # Output: -1.256
print("Exponentiation:", exponentiation_float)  # Output: 9.8596


########################################################################################################################   Strings
name = "Alice"
message = 'Hello, World!'

# String operations
concatenation_with_space = name + " " + message
concatenation_no_space = name + message
length_message = len(message)
length_name = len(name)
uppercase_message = message.upper()
lowercase_message = message.lower()
uppercase_name = name.upper()
lowercase_name = name.lower()

print("\n:::::::::::::::::Strings::::::::::::::::::::::")
print("Concatenation without space:", concatenation_no_space)  # Output: AliceHello, World!
print("Concatenation with space:", concatenation_with_space)  # Output: Alice Hello, World!
print("Length of message:", length_message)  # Output: 13
print("Length of name:", length_name)  # Output: 5
print("Uppercase message:", uppercase_message)  # Output: HELLO, WORLD!
print("Lowercase message:", lowercase_message)  # Output: hello, world!
print("Uppercase name:", uppercase_name)  # Output: ALICE
print("Lowercase name:", lowercase_name)  # Output: alice

# Additional string operations
find_world = message.find("World")
replace_hello = message.replace("Hello", "Hi")
split_message = message.split()
strip_message = message.strip('!')

print("\nAdditional String Operations:")
print("Find 'World':", find_world)  # Output: 7
print("Replace 'Hello' with 'Hi':", replace_hello)  # Output: Hi, World!
print("Split message:", split_message)  # Output: ['Hello,', 'World!']
print("Strip '!' from message:", strip_message)  # Output: Hello, World

########################################################################################################################   Booleans
x = True
y = False

# Logical operations
logical_and = x and y
logical_or = x or y
logical_not_x = not x
logical_not_y = not y

print("\n:::::::::::::::::Booleans:::::::::::::::::::::::")
print("Logical AND:", logical_and)  # Output: False
print("Logical OR:", logical_or)  # Output: True
print("Logical NOT x:", logical_not_x)  # Output: False
print("Logical NOT y:", logical_not_y)  # Output: True

########################################################################################################################   Type Checking
print("\n:::::::::::::::::Type Checking:::::::::::::::::::::::")
print("Type of num1:", type(num1))  # Output: <class 'int'>
print("Type of float1:", type(float1))  # Output: <class 'float'>
print("Type of name:", type(name))  # Output: <class 'str'>
print("Type of x:", type(x))  # Output: <class 'bool'>
