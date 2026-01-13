import array
arr1 = array.array('i', [3, 6, 9, 12])
arr2 = array.array('i', arr1)  
print("Original array:", arr1)
print("Copied array:", arr2)