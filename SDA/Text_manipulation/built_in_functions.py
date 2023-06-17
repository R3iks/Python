# len
print(len("Good bye"))

a = "Hello"

# len internal functionality
n = a.index(a[-1]) + 1
print(n)
print(len(a))

# Accesing single letter
print(a[-5])

# Accesign a substring (a collection of strings within another string)
# Slicing
print(a[1:4])

# Step
"""
qwertyuiopasdfghjklzxcvbnm
01234..
...-5,-4,-3,-2,-1
"""
b = "qwertyuiopasdfghjklzxcvbnm"

# Pick all the letters with a step of 2
print(b[::2])

print(b[::-1])

#################

"""
Hello
01234
-5,-4,-3,-2,-1
"""