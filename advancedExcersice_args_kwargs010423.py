# Exercise: Create a function that takes any number of positional and keyword
# arguments and calculates the total cost of items in a shopping cart.

# The function should apply a discount to specific items if provided.

# The function should accept any number of positional arguments representing
# the cost of each item in the cart.

# The function should accept any number of keyword arguments representing discounts 
# for specific items in the cart. The keyword argument's key should be the item's
# index (0-based), and its value should be the discount percentage.

# The function should calculate the total cost by applying the discounts to 
# the specified items and return the result.

"""
1. The function should accept any number of positional arguments representing 
the cost of each item in the cart. (*args) (100, 50, 20, 5)

2. The function should accept any number of keyword arguments representing discounts 
for specific items in the cart. The keyword argument's key should be the item's name 
(name-based), and its value should be the discount percentage. (**kwargs) (0=50, 3=5)

3. The function should calculate the total cost by applying the discounts 
to the specified items and return the result.
"""


def total_cost(*prices, **discounts):
    price = 0

    for name, cost in prices:
        discount = discounts.get(name, 0)
        item_cost = cost * (1 - discount / 100)  # Calculating discount
        price += item_cost

    return price


cost = total_cost(
    ("apple", 100), ("coke", 50), apple=50, coke=20
)  # apple price 100, coke price 50, apple discount 50%, coke discount 20%
print(f"Total cost: {cost:.2f}")