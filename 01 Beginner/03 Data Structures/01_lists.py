# Creating a list
my_list = [1, 2, 'hello', True, 3.14]

####################################################################################################### Accessing elements of a list
print("First element:", my_list[0])  # Access the first element using index
print("Last element:", my_list[-1])  # Access the last element using negative index

####################################################################################################### Slicing a list
print("Sliced elements:", my_list[1:4])  # Slice the list to get elements from index 1 to 3

####################################################################################################### Modifying elements of a list
my_list[2] = 'world'  # Modify the element at index 2
print("Modified list:", my_list)  # Print the modified list

####################################################################################################### Appending an element to the list
my_list.append('new element')  # Append a new element to the end of the list
print("Appended list:", my_list)  # Print the list after appending

####################################################################################################### Removing an element from the list
removed_element = my_list.pop(3)  # Remove and return the element at index 3
print("Removed element:", removed_element)  # Print the removed element
print("Updated list:", my_list)  # Print the updated list after removal

####################################################################################################### Checking if an element exists in the list
print("Is 'hello' in the list?", 'hello' in my_list)  # Check if 'hello' exists in the list

####################################################################################################### Length of the list
print("Length of the list:", len(my_list))  # Get the length of the list

####################################################################################################### Iterating over elements in the list
print("\nIterating over elements in the list:")
for item in my_list:  # Iterate over each item in the list
    print(item)  # Print each item in the list
#####################################################################################################################################################################################################################################################################################################################
