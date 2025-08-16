status = "starting"
attempt = 1

while status != "running":
    print(f"Check {attempt}: Service is {status}")
    # Simulate status change
    if attempt == 3:
        status = "running"
    attempt += 1

print("Service is now running!")