class Person:
    def __init__(self, name, age):
        self.name = name    
        self.age = age

    def greet(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")

p = Person("Alice", 30)
print(p.name)