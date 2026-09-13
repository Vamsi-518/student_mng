def remove_vowels(s: str) -> str:
    return ''.join(ch for ch in s if ch.lower() not in 'aeiou')

print(remove_vowels("interview"))