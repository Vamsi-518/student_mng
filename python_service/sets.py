dev = {"app1", "db1"}
prod = {"app1", "db2"}

print("Common:", dev & prod)

print("Dev-only:", dev - prod)