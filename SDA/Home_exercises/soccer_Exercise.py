"""1 Exercise
Ask the user for their favorite soccer player using the input() function.
"""
""" 2 Exercise
Use string concatenation to create a message that includes the user's favorite soccer team. 
The message should be formatted like this: 
            "Hey there! Your favorite soccer team is the [team]. Go [team]!
"""

favorite_team = input("Please enter your favourite team: ")

cheering_message = (
    "Hey there! Your favorite soccer team is the"
    + favorite_team
    + ". Go"
    + favorite_team
    + "!"
)

print(cheering_message)

"""3 Exercise
# Use printf-style formatting to create a message that includes the user's favorite soccer player. 
The message should be formatted like this: "Nice choice! [player] is an awesome player."
"""

favorite_player = input("Please enter your favourite player: ")
cheering_message_2 = "Nice choice! %s is an awesome." % (favorite_player)
print(cheering_message_2)