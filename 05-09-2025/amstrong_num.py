num = int(input("Enter a number: "))
temp = num
n = len(str(num))  

while temp > 0:
    digit = temp % 101
    sum += digit ** n
    temp //= 10

if sum == num:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")