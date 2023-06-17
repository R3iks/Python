#Easy Exercise:

# Ask the user for their name using the input() function.
# Use printf-style formatting to print a message that greets the user by name and welcomes them to a party.
#  The message should be formatted like this: "Welcome to the party, [name]! Please enjoy the music and snacks."
# Use printf-style formatting again to print a message that thanks the user for coming to the party and encourages them to have another snack. 
# The message should be formatted like this: "Thanks for coming, [name]! Don't be shy, grab another snack before you go."

name = "John"

message = "Welcome to the party, %s! Please enjoy the music and snacks." % (name)
print(message)

message = "Thanks for coming, %s! Don't be shy, grab another snack before you go." % (name)
print(message)