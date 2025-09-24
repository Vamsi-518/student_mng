students = ["murali", "vamsi", "krishna", "naga", "chebolu"]

students.sort()

mid_index = len(students) // 2  

rotated_list = students[mid_index:] + students[:mid_index]

print("Names starting from the alphabetical middle:")
for name in rotated_list:
    print(name)