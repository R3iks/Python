names = ("Jhon", "Elvis", "Tim")
ages = (24, 36, 67)

name = "Jhon"
age = 33
message = "My name is %s and im %d years old." %(name, age)

print(message)

for name, age in zip(names,ages):
    message = "my name is %s and i have %d years old!" % (name, age)
    print(message)
    
#use printf-style to format a string
#message = "my name is %s and i am %d years old." % (name, age)
#print(message)