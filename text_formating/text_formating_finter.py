names = ["Jhon", "Eve", "Alice", "Allan"]
ages = [25, 33, 32, 17]

name = "Jhon"
age = 42

# basic
# Use printf-style to format a string
message = f"My nme is {name} and I am {age} years old."

print(message)

# advanced
for name, age in zip(names, ages):
    message = f"My name is {name} and I have {age} years old!"
    print(message)