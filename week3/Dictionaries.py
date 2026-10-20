# Dictionaries

# 1. Creating a Student Information Dictionary
student = {
    "Name": "Narendra",
    "Age": 20,
    "Course": "B.Tech",
    "City": "Kadapa"
}

print("Student Information:")
print(student)

# 2. Accessing values
print("\nName:", student["Name"])
print("Course:", student["Course"])

# 3. Adding a new key-value pair
student["College"] = "Annamacharya Institute of Technology and Science"
print("\nAfter adding College:")
print(student)

# 4. Updating values
student["Age"] = 21
print("\nAfter updating Age:")
print(student)

# 5. Removing data
student.pop("City")
print("\nAfter removing City:")
print(student)

# 6. Displaying keys and values
print("\nKeys:")
print(student.keys())

print("\nValues:")
print(student.values())

# 7. Using dictionary methods
print("\nNumber of items:", len(student))
print("Is 'Name' present?", "Name" in student)