###################################################################################### Basic Variable Assignment
a = 5
b = 3.14
c = "Hello, World!"
d = True

print("Basic Variable Assignment")
print("a =", a)
print("b =", b)
print("c =", c)
print("d =", d)

###################################################################################### Multiple Assignments
x, y, z = 10, 20.5, "Python"

print("\nMultiple Assignments")
print("x =", x)
print("y =", y)
print("z =", z)

####################################################################################### Swapping Variables
x, y = y, x

print("\nSwapping Variables")
print("After swapping, x =", x)  # Output: 20.5
print("After swapping, y =", y)  # Output: 10

######################################################################################## Type Conversion
e = str(a)  # Convert integer to string
f = int(b)  # Convert float to integer
g = float(y)  # Convert integer to float
h = bool(1)  # Convert integer to boolean

print("\nType Conversion")
print("e (str):", e, type(e))
print("f (int):", f, type(f))
print("g (float):", g, type(g))
print("h (bool):", h, type(h))

######################################################################################## Variable Reassignment
x = 100
print("\nVariable Reassignment")
print("x =", x)

# Using Variables in Expressions
result = a + b
greeting = c + " How are you?"

print("\nUsing Variables in Expressions")
print("result (a + b):", result)
print("greeting (c + ...):", greeting)

######################################################################################## Incrementing/Decrementing Variables
counter = 0
counter += 1  # Increment
counter -= 1  # Decrement

print("\nIncrementing/Decrementing Variables")
print("counter:", counter)

######################################################################################## Global vs. Local Variables
global_var = "I am global"

def some_function():
    local_var = "I am local"
    print("Inside function - global_var:", global_var)
    print("Inside function - local_var:", local_var)

some_function()
# print(local_var)  # This will raise an error

print("\nGlobal vs. Local Variables")
print("Outside function - global_var:", global_var)

######################################################################################## Constants (by convention, in all caps)
PI = 3.14159
GRAVITY = 9.81

print("\nConstants (by convention, in all caps)")
print("PI:", PI)
print("GRAVITY:", GRAVITY)

######################################################################################## Using Variables with Different Scopes
def outer_function():
    outer_var = "outer"

    def inner_function():
        inner_var = "inner"
        print("Inside inner_function - outer_var:", outer_var)
        print("Inside inner_function - inner_var:", inner_var)

    inner_function()
    # print(inner_var)  # This will raise an error

outer_function()

print("\nUsing Variables with Different Scopes")
# print(outer_var)  # This will raise an error

######################################################################################## Dynamic Typing
var = 10
print("\nDynamic Typing")
print("var (initial):", var, type(var))
var = "Now I'm a string"
print("var (changed):", var, type(var))
