import string

s = "Hello@# World!!"
clean = ''.join(char for char in s if char.isalnum() or char.isspace())
print(clean) 