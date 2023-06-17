# 1. Ask the user for the score of a recent soccer match using the input() function.

# 2. Use string manipulation functions to separate the score into two variables representing the number of goals scored by each team. Print the variables.

# 3. Use conditional statements to determine the winner of the soccer match. If the first team won, print a message that congratulates them. 
#If the second team won, print a message that congratulates them. If the match was a draw, print a message that encourages both teams. 
#The messages should be formatted like this: "[team1] wins! Congrats [team1]!" or "[team2] wins! Congrats [team2]!" or "It's a draw! Good job, both teams."

# 4. Ask the user for the total number of goals scored in the match using the input() function.

# 5. Use arithmetic operators to calculate the average number of goals per team. Print the result using printf-style formatting. The message should be formatted like this:
# "The average number of goals per team was %.2f." (where %f is replaced by the calculated average, rounded to 2 decimal places).

# 1 ask the user dor score
score = input("Please enter the score of a recent soccer match (format: team1-team2): ")

# 2 seperate score
team1_goals, team2_goals = map(int, score.split("-"))
print(f"Team 1 goals: {team1_goals}")
print(f"Team 2 goals: {team2_goals}")

# 3 print condicial cheering messages
if team1_goals > team2_goals:
    print(f"Team 1 wins! Congrats Team 1!")
elif team2_goals > team1_goals:
    print(f"Team 2 wins! Congrats Team2")
else:
    print("It's a draw! Good job, both teams.")


# 4 ask the user for total goals
total_goals =int(input("Please eneter the total number of goals scored during the match: "))

# 5 calculate the average number of goals 
average_goals = total_goals / 2

# 2 is the number of teams

print("The average number of goals per team was %.2f" %average_goals)