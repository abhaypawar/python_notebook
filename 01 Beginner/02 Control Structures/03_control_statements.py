############################################################################# Example 1: break statement
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "banana":
        break
    print(fruit)  # Output: apple

############################################################################# Example 2: continue statement
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        continue
    print(num)  # Output: 1, 3, 5

############################################################################# Example 3: pass statement
# The pass statement is a null operation; nothing happens when it executes.
for fruit in fruits:
    if fruit == "banana":
        pass  # This is a placeholder for future code.
    print(fruit)  # Output: apple, banana, cherry

############################################################################# Example 4: else with loops
# The else block runs if the loop completes without encountering a break statement.
for fruit in fruits:
    if fruit == "kiwi":
        break
    print(fruit)
else:
    print("No kiwi found")  # Output: apple, banana, cherry, No kiwi found

############################################################################# Example 5: nested loops with break
# Using break to exit from inner loop only.
for fruit in fruits:
    for char in fruit:
        if char == 'a':
            break
        print(char)  # Output: p, c, h
    print(fruit)  # Output: apple, banana, cherry

############################################################################# Example 6: nested loops with continue
# Using continue to skip current iteration of inner loop.
for fruit in fruits:
    for char in fruit:
        if char == 'a':
            continue
        print(char)  # Output: p, p, l, e, b, n, n, c, h, e, r, r, y
    print(fruit)  # Output: apple, banana, cherry

############################################################################# Example 7: Using break and continue together
# Combining break and continue in a single loop.
for num in range(10):
    if num == 5:
        break
    if num % 2 == 0:
        continue
    print(num)  # Output: 1, 3

############################################################################# Example 8: Using break in a while loop
count = 0
while count < 10:
    if count == 5:
        break
    print(count)  # Output: 0, 1, 2, 3, 4
    count += 1

############################################################################# Example 9: Using continue in a while loop
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue
    print(count)  # Output: 1, 3, 5, 7, 9
