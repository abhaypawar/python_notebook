####################################################################### Creating a set
my_set = {1, 2, 3, 4, 5}

####################################################################### Adding elements to a set
my_set.add(6)
my_set.update([7, 8])
print("Updated set:", my_set)  # Print the updated set

####################################################################### Removing elements from a set
my_set.remove(3)
my_set.discard(10)  # Discard an element (if present)
print("Updated set after removals:", my_set)  # Print the updated set

####################################################################### Checking if an element exists in the set
print("Is 5 in the set?", 5 in my_set)  # Check if 5 exists in the set

####################################################################### Length of the set
print("Length of the set:", len(my_set))  # Get the length of the set

####################################################################### Set operations: union, intersection, difference
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

####################################################################### Union of sets
union_set = set1.union(set2)
print("Union:", union_set)

####################################################################### Intersection of sets
intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)

####################################################################### Difference between sets
difference_set = set1.difference(set2)
print("Difference:", difference_set)

####################################################################### Iterating over elements in the set
print("\nIterating over elements in the set:")
for item in my_set:  # Iterate over elements in the set
    print(item)  # Print each element
##############################################################################################################################################
