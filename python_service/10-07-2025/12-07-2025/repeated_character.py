string = "Welcome the Hyderabad"
for char in set(string.lower()):
    if string.lower().count(char)>1:
        print(char)