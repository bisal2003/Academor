# Create a list
my_list = [1, "hello", 3.14]

# Access elements
print(my_list[0])  # Output: 1
print(my_list[1])  # Output: hello

# Append element
my_list.append("new element")
print(my_list)  # Output: [1, 'hello', 3.14, 'new element']

# Insert element
my_list.insert(1, "inserted element")
print(my_list)  # Output: [1, 'inserted element', 'hello', 3.14, 'new element']

# Remove element by value
my_list.remove("hello")
print(my_list)  # Output: [1, 'inserted element', 3.14, 'new element']

# Remove element by index
popped_element = my_list.pop(2)
print(popped_element)  # Output: 3.14
print(my_list)         # Output: [1, 'inserted element', 'new element']

# Extend list
my_list.extend([2, 4, 6])
print(my_list)  # Output: [1, 'inserted element', 'new element', 2, 4, 6]

# Sort list
numeric_list = [3, 1, 4, 1, 5, 9, 2]
numeric_list.sort()
print(numeric_list)  # Output: [1, 1, 2, 3, 4, 5, 9]

# Reverse list
numeric_list.reverse()
print(numeric_list)  # Output: [9, 5, 4, 3, 2, 1, 1]

# Clear list
my_list.clear()
print(my_list)  # Output: []

# Count elements
repeated_list = [1, 2, 2, 3, 3, 3, 4]
count_of_threes = repeated_list.count(3)
print(count_of_threes)  # Output: 3

# Find index of an element
index_of_two = repeated_list.index(2)
print(index_of_two)  # Output: 1

# Copy list
copied_list = repeated_list.copy()
print(copied_list)  # Output: [1, 2, 2, 3, 3, 3, 4]







