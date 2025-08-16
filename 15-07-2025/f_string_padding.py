students = [("Alice", 89), ("Bob", 72), ("Charlie", 95)]
print(f"{'NAME':<10} {'SCORE':<7} {'GRADE'}")
print("-" * 25)
for name, score in students:
    grade = 'A' if score >= 90 else ('B' if score >= 80 else 'C')
    print(f"{name:<10} {score:<7d} {grade}")