num = int(input("Enter a number: "))
total = sum(int(d)**3 for d in str(num))
if total == num:
    print("Armstrong Number")
else:
    print("Not Armstrong")