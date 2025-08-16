import keyword

# Print all Python keywords
print("List of Python keywords:")
keywords = keyword.kwlist
print(keywords)

# Print total number of keywords
print("\nTotal number of keywords:", len(keywords))

# Check if specific words are keywords
words_to_check = ["if", "else", "hello", "try", "main"]
print("\nKeyword Check:")
for word in words_to_check:
    if keyword.iskeyword(word):
        print(f"'{word}' is a Python keyword.")
    else:
        print(f"'{word}' is NOT a Python keyword.")
