############################################################################################################ Creating a tuple
my_tuple = (1, 2, 'hello', True, 3.14)

############################################################################################################ Accessing elements of a tuple
print("First element:", my_tuple[0])  # Access the first element using index
print("Last element:", my_tuple[-1])  # Access the last element using negative index

############################################################################################################ Slicing a tuple
print("Sliced elements:", my_tuple[1:4])  # Slice the tuple to get elements from index 1 to 3

############################################################################################################ Tuples are immutable, so modifying elements is not allowed
# Uncommenting the line below will raise an error
# my_tuple[2] = 'world'

############################################################################################################ Checking if an element exists in the tuple
print("Is 'hello' in the tuple?", 'hello' in my_tuple)  # Check if 'hello' exists in the tuple

############################################################################################################ Length of the tuple
print("Length of the tuple:", len(my_tuple))  # Get the length of the tuple

############################################################################################################ Iterating over elements in the tuple
print("\nIterating over elements in the tuple:")
for item in my_tuple:  # Iterate over each item in the tuple
    print(item)  # Print each item in the tuple
######################################################################################################################################################################################################################
