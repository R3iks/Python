name = "Jhon"
age = 25

# Use the sep parameter to change the separator between values
print("whatever text", name, "and I have", age, " years old!", sep="----")


# Use the end paramerer to change the ending parameter
print("This is the first line", end=" ")
print("This is the second line")

# Advanced topics - We are going to explain it later on the course
# Use the file parameter to write output to a file
text_contents = "Hi how are you doing, welcome to SDA academy Python the basics"
with open("output.txt", "w") as file:
    print(text_contents, file=file)

# Use the flush parameter to flush the output buffer immediately
for i in range(5):
    print("This is line", i + 5, flush=True)