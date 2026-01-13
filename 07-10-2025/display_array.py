import array
arr = array.array('i', [10, 20, 30, 40, 50])
print("Array elements:")
for i in arr:
    print(i, end=" ")
print("\nFirst element:", arr[0])
print("Last element:", arr[-1])