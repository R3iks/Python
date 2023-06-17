# single inheritance, Multiple inheritance, Multilevel inheritance
# The goal of inheritance is to write less code (DRY) and have clear and separate logic

# Single inheritance example
class Parent:
    def __init__(self, a) -> None:
        self.a = a + "from parent"

    def greet(self):
        print("Hello from parent")


class Child(Parent):
    pass


child = Child("Argument ")

child.greet()
print(child.a)

# Multiple inheritance


class Parent1:
    def greet(self):
        print("Hello from paren1!")

    def goodbye1(self):
        print("Goodbye from parent1!")


class Parent2:
    def greet(self):
        print("Hello from parent2!")

    def goodbye2(self):
        print("Goodbye from part2!")


class Child(Parent2, Parent1):  # First inheritances overwrites the second ones
    pass


child = Child()

child.greet()

### Multilevel inheritance


class Grandparent:
    def greet(self):
        print("Hello from Grandparent!!")


class Parent(Grandparent):
    pass


class Child(Parent):
    pass


child = Child()

child.greet()

## Hierarchical inheritance


class Parent:
    def greet(self):
        print("Hello from Parent!!")


class Child1(Parent):
    pass


class Child2(Parent):
    pass

class Child3(Parent):
    pass


child1 = Child1()
child2 = Child2()
child3 = Child3()

child1.greet()
child2.greet()
child3.greet()