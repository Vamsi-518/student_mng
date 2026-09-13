import array
arr = array.array('i', [10, 20, 30, 40, 50])
total = sum(arr)
avg = total / len(arr)
print("Array:", arr)
print("Sum:", total)
print("Average:", avg)