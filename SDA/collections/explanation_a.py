# COLLECTIONS
print("Welcome to the Python colections introduction!")

# list []
print("\n1. Lists")
print("List are ordered, mutable, and can contain mixed data types")
fruits = ["apple", "banana", "orange"]
print("Example list :", fruits)

# Methods of the list
"""
.count(x)
.index(x)
.insert(index, x)
.pop(index)
.pop()
.remove(x)
.clear()
.reverse()
"""
# Adding an element to the list
fruits.append("grape")
print("After adding 'grape': ", fruits)

# Accessing elements by index
print("First element (index 3): ", fruits[3])

# Tuples
print("\n2. tuples")
print("Tuples are ordered, immutable, and can contain mixed data types")
colors = ("White", "Blue", "Black")
print("Example tuple (colors): ", colors)

# Accesing elements by index
print("Second element (index 1): ", colors[1])


# Diccionaries
print("\n3 Diccionaries")
print(
    "Diccionaries are unordered, mutable, and contains key:value pairs, it can contain mixed data types"
)
ages = {"John": 30, "Alice": 25, "Bob": 28}
print("Example dictionary (ages)", ages)

# Accesing elements by key
print("Jhon's age: ", ages["John"])
print("Jhon's age: ", ages.get("John", "User not in database"))

# Adding a new key-value pair
ages["Cindy"] = 22
print("After adding 'Cindy'", ages)

# Sets
print("\n4 Sets")
print("Sets are unordered, mutable, and store unique elements.")
numbers = {1, 2, 3, 4, 4, 4}

print(numbers)  # 1, 2, 3, 4
print("Example set (numbers): ", numbers)

# Adding an element to the set
numbers.add(5)
print("After adding 5: ", numbers)

# Checking if an element is in the set (You can do that with all the collections)
print("3 is in the set?", 3 in numbers)

print("\n That's it! Now you know the foundations of collections")







#[1, 2, 3, 4]
#a = [11, 11.3, "String", False, [1, 2, 3,]]

#print(a[::2])

# Methods of the list
# empty_list = []
# empty_list.append(True)
# empty_list.append(1)
# empty_list.append(33.5)
# empty_list.append("Another string")

# empty_list.clear()

#another_list = [1, 3, 1, 8, 2, 2, 2, 2, 3, 9, 3, 3]
#another_list.count(2) #2
#yet_another_list = [True, True, True]

# another_list.extend(
#     yet_another_list
#     )           #output: [1, 1, True, True, True, 2, 2, 2, 2, 3, 3, 3, 3, 8, 9]

#another_list.sort()
# print(sorted(another_list))

#print(another_list)
