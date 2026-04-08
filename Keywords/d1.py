student = {"name": "John Doe", "age": 20, "major": "Science"}
print(student["name"])  # Output: John Doeprint(student["age"])   # Output: 20
print(student["major"]) # Output: Science
print(student["age"])
for key in student:
    print(key)  # Output: name, age, major

student["age"] = 30
print(student["age"])  # Output: 30
student["gpa"] = 3.5
for key, value in student.items():
    print(f"{key}: {value}")

