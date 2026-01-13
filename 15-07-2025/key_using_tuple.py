from collections import defaultdict

def group_records(records: list[tuple[str, int]]) -> dict[str, list[int]]:
    grouped = defaultdict(list)
    for key, val in records:
        grouped[key].append(val)
    return grouped

data = [('Alice', 85), ('Bob', 90), ('Alice', 95), ('Bob', 88)]
print(group_records(data))