list_to_populate_a = []  # just an epty list

"""append logic

a = []

a.append(1)

***internally***
a = [1,2,3] --> memory

original memory:
    index: 0, 1, 2
    values: 1, 2, 3

a.append(4)

values index methods(append, insert...) # memory objects

uodated memory: # After the append
    index: 0, 1, 2, 3
    values: 1, 2, 3, 4

******

"""
# List
# Tradicional way of populating a list
for number in range(10):
    list_to_populate_a.append(number)

print(list_to_populate_a)

# List comprehension way of populating a list
list_to_populate_b = [number for number in range(10)]
print(list_to_populate_b)



# Dictionary comprehensions
list_to_populate_c = {number: number ** 2 for number in range(1, 6)}
# Set comprehensions
list_to_populate_b = {number for number in range(10)}
# Generator comprehensions -- Not in SDA Test
list_to_populate_b = (number for number in range(10))
# Tuple comprehensions
list_to_populate_b = tuple(number for number in range(10))