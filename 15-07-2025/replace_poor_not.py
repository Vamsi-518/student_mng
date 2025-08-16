def replace_not_poor(s):
    n = s.find("not")
    p = s.find("poor")
    if n != -1 and p != -1 and p > n:
        return s[:n] + "good" + s[p+4:]
    return s

print(replace_not_poor("The music is not that poor!"))

print(replace_not_poor("The music is poor!"))