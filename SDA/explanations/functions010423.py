# # This script calculate the sum difference and product of two pairs of numbers
# # Refractor this script using functions
# # The goal is to not repeat code and simplify the code

# # Pair 1
# a, b = 10, 5

# # calculate sum difference, and product for pairs 1
# sum1 = a + b
# diff1 = a - b
# prod1 = a * b

# # Pair 1
# c, d = 7, 3

# # calculate sum difference, and product for pairs 1
# sum2 = c + d
# diff2 = c - d
# prod2 = c * d

# # print the results

# print(f"Pair1 results {sum1}, {diff1}, {prod1}")
# print(f"Pair2 results {sum2}, {diff2}, {prod2}")





# a, b = 10, 5

# def calculation(self, sum, diff, prod):
#     self.sum
#     return sum
#     self.diff = diff
#     return diff
#     self.prod = prod
#     return prod

# sum = a + b
# diff = a - b
# prod = a * b
# print(sum, diff, prod)

# # Pair 1
# c, d = 7, 3

# # calculate sum difference, and product for pairs 1
# sum2 = c + d
# diff2 = c - d
# prod2 = c * d

# # print the results

# print(f"Pair1 results {sum1}, {diff1}, {prod1}")
# print(f"Pair2 results {sum2}, {diff2}, {prod2}")


# KUIDAS OLEMA PEAB


def print_calculations(a, b):
    print(f"Pair results of number: {a} and {b}: {a + b} {a - b} {a * b}")
    return None


# print the results

# print_calculations(10, 5)   võta hiljem maha
# print_calculations(7, 3)



# ADVANCED 

# def example_args(*args):
#     print(args)


# def example(**example_kwargs):
#     if "id" in example_kwargs.keys():
#         id_user = example_kwargs.get("id", "Null")
#         print(f"your id is {id_user}")

#     name = example_kwargs.get("name", "Null")
#     surname = example_kwargs.get("surname", "Null")
#     age = example_kwargs.get("age", "Null")

#     print(f"Welcome {name} {surname} you are {age} years old.")
#     return None


# example(a=1, name="Martha", surname="Hopkins", age=99)