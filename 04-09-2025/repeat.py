s = "welcome to hyderabad"
print({c: s.count(c) for c in set(s) if c != ' ' and s.count(c) > 1})