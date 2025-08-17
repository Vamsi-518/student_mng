import array

numbers = array.array('i', [10, 20, 30, 40, 50])

print(numbers[2]) 
print(" ") 

numbers.append(60)

numbers.remove(20) 

for num in numbers:
    print(num)