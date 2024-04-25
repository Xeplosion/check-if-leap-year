# Foster Cavender
# CS1400 online 7 week

import math

# variables for later
indent = "    "

# welcome the user
print("Hello beautiful and welcome to the amazing, one of a kind leap year calculator!")

# prompt the user for a year
year = int(input(indent + "Enter a year to find out if it's a leap year: "))
print("")

# pre-calculations
firstTwo = math.floor(year / 100)
lastTwo = str(year)[2] + str(year)[3]
sumLastTwo = int(lastTwo[0]) + int(lastTwo[1])

# pre-written output messages
messages = [
    "Thanks for using the amazing leap year calculator! \n" + indent + "Your year, " + str(year) + ", is not a leap year sorry... :(",
    "Thanks for using the amazing leap year calculator! \n" + indent + "Your year, " + str(year) + ", is a leap year! :)"
]

# calculate result
if year % 9 == 0 and lastTwo[0] != lastTwo[1]:
    print(messages[1])
elif sumLastTwo == firstTwo and int(lastTwo[0]) % 2 == 0 and int(lastTwo[0]) < int(lastTwo[1]):
    print(messages[1])
else:
    print(messages[0])