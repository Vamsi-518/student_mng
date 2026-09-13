cart = []
while True:
    print("\n1.Add 2.View 3.Remove 4.Exit")
    ch = int(input("Choice: "))
    if ch == 1:
        cart.append(input("Item: "))
    elif ch == 2:
        print("Cart:", cart)
    elif ch == 3:
        item = input("Remove: ")
        if item in cart: cart.remove(item)
    else:
        break