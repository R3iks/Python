# Hard Exercise:
# 1. Ask the user for their name and age using the input() function.
name = input("What's your name? ")
age = float(input("How old are you? "))  # Change datatype to float to use in formula

"""2 .Use printf-style formatting to print a message that tells 
the user how old they will be in 10 years. The message should be 
formatted like this: 

    "Hey [name], did you know that in 10 years you'll be %d years old?!" 
    
    (where %d is replaced by the calculated age).
"""

future_age = age + 10
age_message = "Hey %s, did you know that in 10 years you'll be %d years old?!" % (
    name,
    future_age,
)


"""3. Use printf-style formatting again to print a message that calculates 
the user's BMI (Body Mass Index) based on their height and weight. 

Ask the user to enter their height in meters and their weight in kilograms, 
and then use the following:
 formula to calculate their BMI: BMI = weight / (height * height). 
 
 The message should be formatted like this: "Wow, [name], your BMI is %.2f. 
 You might want to cut back on the snacks at the party!" 
 (where %.2f is replaced by the calculated BMI value, rounded to 2 decimal places)."""

# Ask the user for their heigh ad weight

height = float(input("What is your height in meters? "))
weight = float(input("What is your height in kilograms? "))

# Calculate the user's BMI and print the message using print=f style
bmi = weight / (height * height)
bmi_message = (
    "Wow, %s, your BMI is %.2f. You might want to cut back on the snacks at the party!"
    % (name, bmi)
)
print(bmi_message)


"""4. Use printf-style formatting one more time to print a message that gives the 
user a nickname based on their name and BMI. If their BMI is less than 18.5, 
give them the nickname "Slim [name]". 

If their BMI is between 18.5 and 24.9, give them the nickname "Fit [name]". 
If their BMI is between 25 and 29.9, give them the nickname "Chonky [name]". 
If their BMI is 30 or higher, give them the nickname "Big [name]". 

The message should be formatted like this: 

"Hey there, %s! From now on, we'll call you %s." 

(where %s is replaced by the user's name and their new nickname)."""

if bmi < 18.5:
    nickname = f"Slim {name}"
elif bmi >= 18.5 and bmi <= 24.9:
    nickname = f"Fit {name}"
elif bmi >= 25 and bmi <= 29.9:
    nickname = f"Chonky {name}"
else:
    nickname = f"Big {name}"

nickname_mesagge = "Hey there, %s! From now on, we'll call you %s." % (name, nickname)

print(nickname_mesagge)