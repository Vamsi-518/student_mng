nums = [1,2,2,3,4,4,5,6,6,7]
unique = []
for n in nums:
    if n not in unique:
        unique.append(n)
print("Original:", nums)
print("Unique:", unique)