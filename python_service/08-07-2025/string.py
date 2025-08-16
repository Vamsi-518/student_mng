# Define a string
name = "PythonProgramming"

# Print original string
print("Original String:", name)

# String Length
print("Length:", len(name))

# Uppercase
print("Uppercase:", name.upper())

# Lowercase
print("Lowercase:", name.lower())

# First 6 characters
print("First 6 characters:", name[:6])

# Last 6 characters
print("Last 6 characters:", name[-6:])

# Reverse string
print("Reversed:", name[::-1])

# Replace part of the string
print("Replace 'Python' with 'Java':", name.replace("Python", "Java"))

# Check if a substring exists
print("Does it contain 'gram'?", "gram" in name)
