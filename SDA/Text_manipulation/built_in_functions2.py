# # tring indexes
# # string[start:stop:step]
a = "Hello"
# # Accesing single letter
print(a[-5])

# # Accesign a substring (a collection of strings within another string)
# # Slicing
print(a[1:4])

# # Step
# """
# qwertyuiopasdfghjklzxcvbnm
# 01234..
# ...-5,-4,-3,-2,-1
# """
b = "qwertyuiopasdfghjklzxcvbnm"

# # Pick all the letters with a step of 2
print(b[::2])

print(b[::-1])

# #################

# """
# Hello
# 01234
# -5,-4,-3,-2,-1
# """

# ########### Built in functions
# # len
print(len("Good bye"))


# # len internal functionality
n = a.index(a[-1]) + 1
print(n)
print(len(a))

# index -> Gives you the index of a substring
print("Hello World".index("W"))

# count --> Counts all the number of a input letter inside a string
print("112233334455555555".count("3"))

# upper and lower --> Caps all the letters from the string
print("hello".upper())
print("HELLO".lower())

print("Hello"[0].lower())