n = int(input("Enter number: "))
rev = 0
while n:
    rev = rev * 10 + n % 10
    n //= 10
print("Reversed:", rev)