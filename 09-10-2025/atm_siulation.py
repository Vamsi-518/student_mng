# loops, conditionals, functions using

balance = 5000
while True:
    print("\n1.Deposit 2.Withdraw 3.Balance 4.Exit")
    ch = int(input("Choose: "))
    if ch == 1:
        amt = int(input("Amount: "))
        balance += amt
    elif ch == 2:
        amt = int(input("Amount: "))
        if amt <= balance:
            balance -= amt
        else:
            print("Insufficient funds")
    elif ch == 3:
        print("Balance:", balance)
    else:
        break
