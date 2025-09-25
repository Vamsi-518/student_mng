s = "hello world"
vowels = "aeiouAEIOU"
res = "".join("*" if ch in vowels else ch for ch in s)
print(res)
