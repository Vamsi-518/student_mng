import array
arr = array.array('i', [1, 2, 3, 4])
print("Original:", arr)
arr.insert(2, 99)   
print("After insert:", arr)
arr.remove(3)       
print("After remove:", arr)