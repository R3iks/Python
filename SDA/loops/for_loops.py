# For loops

"""syntax
for variable in iterable:
    intruction 1
    instruction 2
    instruction 3
    ...

"""


"""Example 1 - iterating over values of a collection

1st iteration
    word = 'Hi'
2nd iteration
    word = 'how'
3rd iteration
    word = 'are'
...

"""
# iterating in an iterable
iterable = ["Hi", "how", "are", "you", "?"]
for word in iterable:
    print(word)

""" Example 2 - iteration x amount of times

range syntax --> range(start:stop:step)
range(3) --> [1, 2, 3]

1st iteration --> _ = 1
2nd iteration --> _ = 2
3rd iteration --> _ = 3

"""

# iterating x amount of times
for _ in range(3):
    print("Hello world!")