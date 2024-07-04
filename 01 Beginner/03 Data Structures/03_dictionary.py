######################################################################################### Creating a dictionary
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

######################################################################################### Accessing values in a dictionary using keys
print("Name:", my_dict['name'])  # Access value using key 'name'
print("Age:", my_dict['age'])  # Access value using key 'age'

######################################################################################### Adding new key-value pairs to the dictionary
my_dict['email'] = 'alice@example.com'
print("Updated dictionary:", my_dict)  # Print the updated dictionary

######################################################################################### Modifying values in the dictionary
my_dict['age'] = 35  # Modify the value associated with key 'age'
print("Modified dictionary:", my_dict)  # Print the modified dictionary

######################################################################################### Removing a key-value pair from the dictionary
removed_value = my_dict.pop('city')  # Remove and return the value associated with key 'city'
print("Removed value:", removed_value)  # Print the removed value
print("Updated dictionary:", my_dict)  # Print the updated dictionary after removal

######################################################################################### Checking if a key exists in the dictionary
print("Is 'email' in the dictionary?", 'email' in my_dict)  # Check if 'email' key exists in the dictionary

##########################################################################################Length of the dictionary (number of key-value pairs)
print("Length of the dictionary:", len(my_dict))  # Get the length of the dictionary

######################################################################################### Iterating over keys and values in the dictionary
print("\nIterating over keys and values in the dictionary:")
for key, value in my_dict.items():  # Iterate over key-value pairs in the dictionary
    print(f"Key: {key}, Value: {value}")  # Print each key-value pair
