# Sets

# 1. Creating a set
numbers = {1, 2, 3, 4, 5, 5, 3}
print("Set:", numbers)

# 2. Removing duplicate values
print("Duplicates removed:", numbers)

# 3. Adding an element
numbers.add(6)
print("After adding 6:", numbers)

# 4. Removing an element
numbers.remove(2)
print("After removing 2:", numbers)

# Two sets for set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# 5. Union
print("Union:", set1.union(set2))

# 6. Intersection
print("Intersection:", set1.intersection(set2))

# 7. Difference
print("Difference:", set1.difference(set2))