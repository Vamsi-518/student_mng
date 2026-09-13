command = "start"

match command:
    case "start":
        print("Starting the system...")
    case "stop":
        print("Stopping the system...")
    case "restart":
        print("Restarting...")
    case _:
        print("Unknown command")