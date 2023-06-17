# n = 2

# while n == 2:
#     print("Hi there!")
#     JOOKSEB LÕPPMATUSSE

# n = 0

# while n < 2:
#     n = n + 1
#     print("Hi there!")          #  PRINDIB KAKS HI THERE 


# While loops

"""Syntax

while condition:
    instruction 1
    instruction 2
    instruction 3
    ...
"""


""" Example 1 ==>  While loops
First iteration n = 0 --> condition is True
Second iteration n = 1 --> coindition is True
Third iteration n = 2 --> condition is false 
"""
n = 0

while n < 2:  # --> False
    n = n + 1  # n = n + 1
    print("Hi there!")  # --> "Hi there!", "Hi there"


""" Example 2 ==> While loops
First iteration condition is False
This code never executes
"""
while False:
    print("Hi there!")


""" Example 3 ==> While loops
First iteration condition is True
Second iteration --> condition is True
...
Infinite
To stop the iterations press Ctrl + C
"""
while True:
    print("Hi there!")


""" Example 4 ==> While loops - break
First iteration n = 1 --> condition is True
Second iteration n = 2 --> condition is True
The internal condition if n == 2 is met
    the break keyword ends the iteration
"""
n = 0
while True:
    n = n + 1
    if n == 2:
        break
    print("Hi there!")



""" Example 5 ==> While loops - continue
First iteration n = 1 --> condition is True
Second iteration n = 2 --> condition is True
Third iteration n = 3 --> condition is True
    The internal condition if n == 3 is met
        the continue keyword doesnt let the 65-69 lines are not executed
Forth iteration n = 4 --> condition is True
    the internal condition (if n == 4) is true
        the break keyworkd ends the loop

"""
n = 0
while True:
    n = n + 1
    if n == 3:
        continue
    if n == 4:
        break
    print("Hi there!")