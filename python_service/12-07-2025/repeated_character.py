string = "Welcome the Hyderabad"
for char in set(string.lower()):
    count = string.lower().count(char)
    print(f"{char}: {count}")