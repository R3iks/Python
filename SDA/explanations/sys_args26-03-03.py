import sys
import random

# # This program gives you compliments

# name = sys.argv[1]
# color = sys.argv[2]

# adjective = ["amazing", "lit", "brilliant", "awesome", "cool", "fantastic"]
# compliments = [
#     f"{name} you're as {random.choice(adjective)} as the color {color}",
#     f"{name}, your {color} aura is so {random.choice(adjective)}",
#     f"Wow, {name}! You're as {random.choice(adjective)} as a {color} rainbow!",
# ]


# if len(sys.argv) != 3:
#     print("Usage: python sys_args.py <>your_name> <favorite_color>")
# else:
#     print(random.choice(compliments))



# Peab vajutama up arrow ja sisetama parameetrid (nimi ja värv)

animal = sys.argv[1]
color = sys.argv[2]

adjective = ["dangerous", "funny", "big", "fat", "skinny"]
compliments = [
    f"{animal} {color} color is as {random.choice(adjective)} as it is {random.choice(adjective)}",
    f"{animal} may come across {random.choice(adjective)}  especially it's color {color} but not to worry, its completely harmless",
    f"Being {random.choice(adjective)} for the {animal} is absolutely fine because their harmless",
]

if len(sys.argv) != 3:
    print("Usage: python sys_args.py <>animal> <color>")
else:
    print(random.choice(compliments))