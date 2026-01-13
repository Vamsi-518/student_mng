arr = [10, 20, 30, 40, 50]

print("First element:", arr[0])

arr[2] = 99
print("Modified array:", arr)

arr.append(60)
print("After append:",arr)

arr.remove(20)
print("After remove:",arr)

for x in arr:
    print(x, end=" ")