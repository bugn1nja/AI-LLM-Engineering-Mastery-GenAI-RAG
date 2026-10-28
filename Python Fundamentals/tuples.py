name_without_tuple = ['John', 'Alice', 'Bob', 'Eve']

# we can edit the list by adding a new name
name_without_tuple.append('Charlie')

# we can also remove a name from the list, because lists are mutable

namw_with_tuple = ('John', 'Alice', 'Bob', 'Eve')

# we cannot edit the tuple by adding a new name, because tuples are immutable

print(f"List of names without tuple: {name_without_tuple}")
print(f"Tuple of names with tuple: {namw_with_tuple}")