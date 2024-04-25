# Foster Cavender
# CS1400 online 7 week

# imports
import random

# variables for later
indent = "    "

# welcome the user
print("Hello and welcome to Foster's Amazing Animal Machine!")

# animal class
class Animal:
    def __init__(self, type, number, says):
        self.type = str(type)
        self.number = int(number)
        self.says = str(says)

# ask about the animals seen
animals = []
numbers = ["first", "second", "third"]
for x in range(0, 3):
    animals.append(Animal(
        input(indent + "What was the " + numbers[x] + " type of animal that you saw? "),
        input(indent + "How many of them did you see? "),
        input(indent + "What sound did they make? ")
    ))
    print("")

# enter prompt
print("Calculating Amazing Animal Machine Report...")
input(indent + "Hit enter to see the results. ")
print("")

# Foster's Amazing Animal Machine report
totalAnimals = animals[0].number + animals[1].number + animals[2].number
average = totalAnimals // 3
animalNames = [animals[0].type, animals[1].type, animals[2].type]

# display report results
print("You saw a whopping " + str(totalAnimals) + " animals! Wow that's a whole lot!")
print("There were " + animalNames[0] + "s, " + animalNames[1] + "s, " + "and " + animalNames[2] + "s.")
for x in range(0, 3):
    print("The " + animalNames[x] + "s all said " + animals[x].says + ".")

print("Now for Foster's Amazing Animal Machine's special creation!")

# special surprise creation :)
typeRandom = ""
for x in range(0, 3):
    word = animals[x].type
    word_list = list(word)
    random.shuffle(word_list)
    typeRandom += "".join(word_list)

saysRandom = ""
for x in range(0, 3):
    word = animals[x].says
    word_list = list(word)
    random.shuffle(word_list)
    saysRandom += "".join(word_list)

print(indent + "You've been gifted " + str(average) + " " + typeRandom + "s that all say" + saysRandom + ".")

