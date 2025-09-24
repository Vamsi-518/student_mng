fruits = ["apple", "banana", "cherry"]

fruits.append("orange")

fruits.remove("banana")

fruits[1] = "blueberry"

print("Fruits list:", fruits)

print("First fruit:", fruits[0])

print("Last fruit:", fruits[-1])

print("First two fruits:", fruits[:2])

for fruit in fruits:
    print("Fruit:", fruit)