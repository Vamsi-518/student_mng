students = {
    "student1": {"name": "Ravi", "age": 21},
    "student2": {"name": "Divya", "age": 22}
}

for key, value in students.items():
    print(key, "=>", value["name"], value["age"])