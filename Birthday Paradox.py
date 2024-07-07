#How many times will a person share a birthday with someone else in a given group of people? The result might seem surprising!

import random
print("Welcome to th birthday paradox! This will tell you how many birthday matches there are for a group of people.")
numberOfBirthdays = input ("How many people are there? ")
numberOfBirthdays = int(numberOfBirthdays)
birthday = []
birthdayDates = [numberOfBirthdays]

def generateBirthday():
    month = random.randint(1, 12)
    if month == 2:
        day = random.randint(1, 28)
    elif month == 4 or month == 6 or month == 9 or month == 11:
        day = random.randint(1, 30)
    else:
        day = random.randint(1, 31)

    birthday = [day, month]
    return birthday

def generateBirthdaySet():
    birthdaySet = []
    for i in range(numberOfBirthdays):
        birthday = generateBirthday()
        birthdaySet.append(birthday)
    return birthdaySet

def findSimilarBirthdays(birthdaySetIn):
    counter = 0
    for i in range(len(birthdaySetIn)):
        currentBirthday = birthdaySetIn[i]
        currentMonth = currentBirthday[1]
        currentDay = currentBirthday[0]
        j = i+1
        for j in range(j, len(birthdaySetIn)):
            tempBirthday = birthdaySetIn[j]
            tempMonth = tempBirthday[1]
            tempDay = tempBirthday[0]
            if currentMonth == tempMonth and currentDay == tempDay:
                counter += 1
    return counter

def calculateTotalCombinations(numberOfBirthdays):
    total = float(numberOfBirthdays)/2*(1 + numberOfBirthdays)
    return total

total = calculateTotalCombinations(numberOfBirthdays)
numberOfMatches = findSimilarBirthdays(generateBirthdaySet())


print("There were " +  str(numberOfMatches) + " birthday matches from " + str(numberOfBirthdays) + " people.")


