import array
arr = array.array('i', [50, 10, 40, 30, 20])
print("Original:", arr)
sorted_arr = array.array('i', sorted(arr))
print("Sorted array:", sorted_arr)
