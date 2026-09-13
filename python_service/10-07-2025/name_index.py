names = ["krishna", "naga", "vamsi", "murali", "chebolu"]

start_index = names.index("murali")

rotated = names[start_index:] + names[:start_index]

print("Names (starting from 'murali'):")
for name in rotated:
    print(name)
