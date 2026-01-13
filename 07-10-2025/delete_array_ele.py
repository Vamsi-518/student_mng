import array
arr = array.array('i', [1, 2, 3, 4, 5])
print("Before delete:", arr)
del arr[2] 
print("After deleting index 2:", arr)
arr.pop()   
print("After pop:", arr)