import random

maxGuesses = 10
maxNumberOfDigits = 3

def getSecretNumber():
    digits = list('0123456789')
    random.shuffle(digits)
    generatedNumber = ''
    for i in range(maxNumberOfDigits):
        generatedNumber += str(digits[i])
    return generatedNumber

secretNumber = getSecretNumber()


def playGame():
    numberOfGuesses = 0
    correct = False
    while numberOfGuesses < maxGuesses and correct == False:
        guess = input("Guess the number: ")
        correct = answerCheck(guess)
        numberOfGuesses = numberOfGuesses + 1
        if numberOfGuesses == 11:
            print("Unlucky! You ran out of guesses.")

def answerCheck(guess):
    if guess == secretNumber:
        print("Congratulations! You correctly guessed the number!")
        return True

    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNumber[i]:
            clues.append("Fermi")
        elif guess[i] in secretNumber:
            clues.append("Pico")
    if len(clues) == 0:
        print("Bagels")
    else:
        clues.sort()
        print(' '.join(clues))

    return False

playGame()