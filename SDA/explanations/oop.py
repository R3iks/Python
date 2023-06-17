 # define a function
def car(brand, kw):
    print(f"brand: {brand}, kw: {kw}")
    return None


# Syntax of the definicion of a class


class Car:
    def __init__(self, brand, kw):  # constructor method
        self.brand = brand
        self.kw = kw

    def print_info(self):
        print(f"brand: {self.brand}, kw: {self.kw}")


mercedes = Car("Mercedes", 500)  # Saves in a memory address

# Functional version
car("Mercedes", 500)

# OOP version
mercedes.print_info()

# Fucntional Good for distributed services
# OOP good for single environments services


# Basic vs functional