# #The goal is to create a “fruit salad” from various fruits and their quantities, then calculate the total weight of the fruit salad.
# #Instructions:
# # 1.Create a list of tuples, where each tuple contains a fruit name and its weight (in grams) per piece.
# Fruit_salad = ("Banana"-200 "grams", "Apple"-300 "grams", "Mango"-500 "grams", "Pear"-600 "grams")
# print("Fruit salad ingredients:", Fruit_salad)
# # 2.Create a dictionary that contains each fruit’s name as the key and the quantity of that fruit in the salad as the value.
# Quantity = {"Banana": 2, "Apple": 4, "Mango": 7, "Pear": 1}
# print("Quantity", Quantity)
# # 3.Calculate the total weight of the fruit salad using the list of tuples and the dictionary.
# Total_weight = Fruit_salad["Banana"]*Fruit_salad[0][1] + Fruit_salad["Apple"]*Fruit_salad[1][2] + Fruit_salad["Mango"]*Fruit_salad[2][3]
# # 4.Print the fruit salad’s ingredients and their quantities.


#ÜLEVAL MINU KÄKK, ALL LAHENDUS####################################


# # 5.Print the total weight of the fruit salad.

# Create a list of tuples, where each tuple contains a fruit name and its weight (in grams) per piece.
fruit_weights = [
    ("apple", 150),
    ("banana", 120),
    ("strawberry", 200)
]


# Step 2: Create a dictionary with fruit names as keys and their quantities in the salad as values
fruit_quantities = {
    "apple": 3,
    "banana": 2,
    "strawberry": 3,
}

# Step 3: Calculate the total weight of the fruit salad
total_weight = fruit_weights[0][1] * fruit_quantities.get("apple") + fruit_weights[1][1] * fruit_quantities.get("banana") + fruit_weights[2][1] * fruit_quantities.get("strawberry")

# Step 4: Print the fruit salad's ingredients and their quantities
print(f"\nTotal wight of the fruit salad: {total_weight}")