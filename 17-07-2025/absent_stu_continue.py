students = ['Vamsi', 'Ramesh', 'Kathikeya', 'Absent', 'Kotesh', 'Hemanth']

for student in students:
    if student == 'Absent':
        continue
    print(f"{student} is present")