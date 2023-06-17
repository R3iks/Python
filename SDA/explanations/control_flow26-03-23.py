# if else elif
""" concept

Tools for controling the executions of the program we are building

Logic:

if condition: # Executes if condition met
    intruction
elif condition: # Executes if previous condition doesn't met and add another condition
    another_instruction
else: # Executes if previous condition doesn't met
    another_else_instruction

syntax:
if condition:
    instructions

thi is not executed in the if

if condition1:
    print("1")
elif condition2:
    print("2")
else:
    print("3")

if condition1:
    print("4")

condition1 is met what would be the output?

"1"
"4"


"""
import getpass

user = "admin"
password = "123"


# Use a while loop to give maximum 3 intents

intents_number = 0

while intents_number < 3:
    intents_number += 1
    user_input = input("Please write your username: ")
    password_input = getpass.getpass("Please write your password: ")

    # Check if user and password are correct
    if user_input == "admin" and password_input == "123":
        print("Welcome admin")
        break
    else:
        print("bad password")


if intents_number == 3:
    print("Try again in 5 minutes")

# n = 3
# if n < 1000000:
#     print("1")
# if n < 10000:
#     print("2")
# if n < 100:
#     print("3")
# output:
# 1
# 2
# 3

# n = 3
# if n < 1000000:
#     print("1")
# elif n < 10000:
#     print("2")
# elif n < 100:
#     print("3")
# output:
# 1