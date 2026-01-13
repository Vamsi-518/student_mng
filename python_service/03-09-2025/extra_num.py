s = "abc123xyz456"
numbers = ''.join([ch for ch in s if ch.isdigit()])
print(numbers)