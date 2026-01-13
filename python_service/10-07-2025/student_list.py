"""take a student list it has 5 student names and display all names in Python"""
student_lists = ["krishna", "vamsi", "naga", "murali", "chebolu"]
"""name should be alphabetical

["murali", "vamsi", "naga", "krishna", "chebolu"]

"""

for i, name in enumerate(student_lists , start=1):
    print(f"student {i}:{name}")

for  name in student_lists:
    print(f"student :{name}")
