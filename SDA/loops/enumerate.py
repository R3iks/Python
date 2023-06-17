a = ["first", "second", "third", "forth", "fifth"]


# Example showing what enumerate does
# for index, value in enumerate(a):
#     print(f"Index: {index}, Value: {value}")


# Useful for simplifying list modifications in a loop
# This version is cleaner and faster in time complexity and memory complexity
for index, value in enumerate(a):
    if value == "third":
        a[index] = "modification"

# This version is less clean and slower
for index in range(len(a)):
    if a[index] == "third":
        a[index] = "modification"

print(a)