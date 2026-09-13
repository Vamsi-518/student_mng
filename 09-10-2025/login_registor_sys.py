# Login and  Register System using File Handling.

def register():
    u = input("Username: ")
    p = input("Password: ")
    open("users.txt", "a").write(f"{u},{p}\n")
def login():
    u = input("Username: ")
    p = input("Password: ")
    data = open("users.txt").read().splitlines()
    print("Login Success" if f"{u},{p}" in data else "Invalid")
register()
login()
