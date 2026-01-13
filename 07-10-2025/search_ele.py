import array
arr = array.array('i', [5, 10, 15, 20, 25])
x = 15
if x in arr:
    print(x, "found at index", arr.index(x))
else:
    print(x, "not found")

