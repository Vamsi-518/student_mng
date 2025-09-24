def invert_dict(d):
    return {v: k for k, v in d.items()}

print(invert_dict({"a":1, "b":2}))
# {1:'a', 2:'b'}