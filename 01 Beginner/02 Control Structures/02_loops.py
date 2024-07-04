############################################################################# Example 1: for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

############################################################################# Example 2: while loop
count = 0
while count < 5:
    print(count)
    count += 1

############################################################################# Example 3: for loop with range()
for i in range(5):
    print(f"Range loop index: {i}")

############################################################################# Example 4: Iterating through a dictionary
fruit_colors = {"apple": "red", "banana": "yellow", "cherry": "red"}
for fruit, color in fruit_colors.items():
    print(f"The color of {fruit} is {color}")

############################################################################# Example 5: Using enumerate() in for loop
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")

############################################################################# Example 6: Using zip() to iterate over multiple sequences
vegetables = ["carrot", "potato", "cucumber"]
for fruit, vegetable in zip(fruits, vegetables):
    print(f"Fruit: {fruit}, Vegetable: {vegetable}")

############################################################################# Example 7: Using break statement
for fruit in fruits:
    if fruit == "banana":
        break
    print(fruit)

############################################################################# Example 8: Using continue statement
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)

############################################################################# Example 9: Using else with loops
for fruit in fruits:
    print(fruit)
else:
    print("Finished iterating through the fruits")

############################################################################# Example 10: Nested loops
for fruit in fruits:
    for char in fruit:
        print(char)

############################################################################# Example 11: List comprehensions
squares = [x**2 for x in range(10)]
print("List of squares:", squares)

############################################################################# Example 12: Infinite loop with break condition
count = 0
while True:
    print(count)
    count += 1
    if count == 5:
        break
##########################################################################################################################################################
