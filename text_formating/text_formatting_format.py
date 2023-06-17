names = ["Jhon", "Eve", "Alice", "Allan"]
ages = [25, 33, 32, 17]

name = "Jhon"
age = 42

# basic
# Use printf-style to format a string
message = "My nme is {1} and I am {0} years old {1}.".format(name, age)

print(message)

# advanced
for name, age in zip(names, ages):
    message = "My name is {0} and I have {1} years old!".format(name, age)
    print(message)