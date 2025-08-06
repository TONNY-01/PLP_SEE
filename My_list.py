# Create an empty list n
my_list = []
print("Step 1  empty list:", my_list)

# Append four values one by one
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("Step 2 - after appends:", my_list)

# Insert value 15 at index 1 (second position)
my_list.insert(1, 15)
print("Step 3 - after insert 15:", my_list)

# Extend the list by another list
my_list.extend([50, 60, 70])
print("Step 4 - after extend:", my_list)

# Remove and return the last element
removed = my_list.pop()
print("Step 5 - removed value:", removed)
print("Step 5 - after pop:", my_list)

# Sort in-place
my_list.sort()
print("Step 6 - after sort:", my_list)

# Find the index of the value 30
index_of_30 = my_list.index(30)
print("Step 7 - index of 30:", index_of_30)
