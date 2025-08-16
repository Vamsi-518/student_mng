numbers = [99, 23, 12, 43, 55]

start_index = numbers.index(43)

rotated = numbers[start_index:] + numbers[:start_index]

print("Rotated list (starting with 43):")
print(rotated)