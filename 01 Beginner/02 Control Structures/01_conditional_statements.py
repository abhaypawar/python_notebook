#################################################################### Example 1: Simple if statement
num = 10
if num > 0:
    print("Positive number")

#################################################################### Example 2: if-elif-else statement
num = -5
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")

#################################################################### Example 3: Nested if statements
num = 15
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")

#################################################################### Example 4: Ternary Conditional Operator
num = 7
result = "Positive number" if num > 0 else "Non-positive number"
print("Ternary Conditional Operator Result:", result)

#################################################################### Example 5: Conditional Expressions with Boolean Operators
a = 10
b = 5
if a > 5 and b > 5:
    print("Both numbers are greater than 5")
elif a > 5 or b > 5:
    print("At least one number is greater than 5")
else:
    print("Neither number is greater than 5")

#################################################################### Example 6: Using `match` statements (Python 3.10 and above)
# Note: This is a new feature introduced in Python 3.10
num = 2
match num:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case _:
        print("Other number")

#################################################################### Example 7: Using if statements with logical operations
num = 12
if num % 2 == 0 and num > 10:
    print("Number is even and greater than 10")
elif num % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

#################################################################### Example 8: Using if statements with in keyword for membership testing
char = 'a'
vowels = 'aeiou'
if char in vowels:
    print(f"'{char}' is a vowel")
else:
    print(f"'{char}' is a consonant")
