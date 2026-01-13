class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def details(self):
        print(f"Brand: {self.brand}, Year: {self.year}")

c1 = Car("Toyota", 2020)
c1.details()
