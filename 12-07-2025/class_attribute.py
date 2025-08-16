class Dog:
    species = "Canis familiaris"  # class-level attribute

    def __init__(self, name):
        self.name = name          # instance-level attribute

dog1 = Dog("Buddy")
dog2 = Dog("Molly")
print(dog1.species)  # Canis familiaris
print(dog2.name)        