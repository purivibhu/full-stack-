# Demonstrating the difference between append and extend in Python lists

# Initialize an empty list
my_list = []

# Using append
my_list.append([1, 2, 3])  # Appends the entire list as a single element
print("After append:", my_list)  # Output: [[1, 2, 3]]

# Using extend
my_list.extend([4, 5, 6])  # Extends the list by adding elements from the iterable
print("After extend:", my_list)  # Output: [[1, 2, 3], 4, 5, 6]