student = {
    "name": "krishna",
    "age": 22,
    "course": "DevOps"
}

print("Name:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])

student["grade"] = "A"
print("Updated student info:", student)

print("Student details:")
for key, value in student.items():
    print(key, ":", value)