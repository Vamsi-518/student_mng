students = ["murali", "vamsi", "krishna", "naga", "chebolu"]

students.sort()

middle_index = len(students) // 2
middle_name = students[middle_index]

print("Names with the alphabetical middle name first:")
print(middle_name)

for i, name in enumerate(students):
    if i != middle_index:
        print(name)