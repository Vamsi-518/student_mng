servers = ["server1", "server2", "server3"]

for server in servers:
    print(f"Connecting to {server}...")
    print(f"Updating packages on {server}...")
    print(f"{server} update complete.\n")

print("All servers updated successfully!")