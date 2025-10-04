items = ["apple", "banana", "apple", "orange", "banana", "apple"]
frequency = {}

for item in items:
    frequency[item] = frequency.get(item, 0) + 1

print("Items:", items)
print("Frequency:", frequency)
  