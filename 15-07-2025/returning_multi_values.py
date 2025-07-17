def sum_and_avg(x, y, z):
    s = x + y + z
    return (s, s/3)

S, A = sum_and_avg(3, 8, 5)
print("Sum =", S, "Avg =", A)