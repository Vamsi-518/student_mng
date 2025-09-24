def print_args(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

print_args(1, 2, 3, name="Alice", age=30)