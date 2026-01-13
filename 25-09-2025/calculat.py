def calculator():
    op = input("Enter operation (+, -, *, /): ")
    a = float(input("First number: "))
    b = float(input("Second number: "))

    if op == '+':
        print(a + b) 
    elif op == '-':
        print(a - b)
    elif op == '*':
        print(a * b)
    elif op == '/':
        print(a / b)
    else:
        print("Invalid operation")

calculator()
