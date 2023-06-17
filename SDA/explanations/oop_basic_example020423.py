class CarBrand:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.brand}, {self.model}, {self.year}"


# Create some car brands
toyota = CarBrand("Toyota")
honda = CarBrand("Honda")
bmw = CarBrand("BMW")

# Create some car instances
car1 = Car(toyota, "Corolla", 2020)
car2 = Car(honda, "Civic", 2021)
car3 = Car(bmw, "M3", 2023)

# Print car details
print(car1)
print(car2)
print(car3)