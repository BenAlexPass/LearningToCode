#I've managed to create a game of blackjack. It's not perfect, but it works!
import random

def generateDeck():
    deck = []
    for suit in ("hearts", "spades", "diamonds", "clubs"):
        for rank in range(2,11):
            card = [str(rank), suit]
            deck.append(card)
        for rank in ("A", "J", "Q", "K"):
            card = [rank, suit]
            deck.append(card)
    random.shuffle(deck)
    return deck

deck = generateDeck()

def printCard(card):
    if card[0] in (1, 11):
        number = "A"
    else:
        number = str(card[0])
    suit = card[1]
    if suit == "hearts":
        suit = "♥"
    if suit == "spades":
        suit = "♠"
    if suit == "clubs":
        suit = "♣"
    if suit == "diamonds":
        suit = "♦"

    print("  __")
    print("|"+number+"  |")
    print("| "+suit+" |")
    print("|__"+number+"|")

def printUnknownCard():
    print(" ___")
    print("|?  |")
    print("| ? |")
    print("|__?|")

def printCards(cards):
    for card in cards:
        printCard(card)

def parseCards(cards):
    for card in cards:
        if card[0] in ("J", "Q", "K"):
            card[0] = 10
        if card[0] == "A":
            card[0] = 11
        else: card[0] = int(card[0])
    return cards

def calculateScore(cards):
    total = 0
    parseCards(cards)
    for card in cards:
        total = total + card[0]
    while total > 21:
        for card in cards:
            if card[0] == 11:
                card[0] = 1
                break
        subtotal = 0
        for card in cards:
            subtotal = subtotal + card[0]
        if subtotal == total:
            break
        else:
            total = subtotal
    return total



def calculateDealersScore(initialCard, scoreToBeat):
    dealersCards = []
    dealersCards.append(initialCard)
    print("Dealer:")
    dealersScore = calculateScore(dealersCards)
    while dealersScore < 21:
        if dealersScore > scoreToBeat:
            break
        dealersCards.append(deck.pop())
        dealersScore = calculateScore(dealersCards)
        printCards(dealersCards)
        print("The dealer's score is " + str(dealersScore))
    return dealersScore

def calculatePlayersScore(playersCards):
    playersScore = calculateScore(playersCards)
    print("Your score is " + str(playersScore))
    choice = input("[S]tick or [T]wist? ")
    while choice != "S" and playersScore < 21:
        playersCards.append(deck.pop())
        printCards(playersCards)
        playersScore = calculateScore(playersCards)
        print("Your total is " + str(playersScore))
        if playersScore < 21:
            choice = input("[S]tick or [T]wist? ")
    return playersScore



def main():
    print("Dealer's cards:")
    dealersCard = deck.pop()
    printCard(dealersCard)
    printUnknownCard()
    print("Your cards:")
    playersCards = []
    playersCards.append(deck.pop())
    playersCards.append(deck.pop())
    printCards(playersCards)
    playersScore = calculatePlayersScore(playersCards)
    if playersScore > 21:
        print("Unlucky! You went bust!")
    else:
        dealersScore = calculateDealersScore(dealersCard, playersScore)
        if playersScore > dealersScore or dealersScore > 21:
            print("Congratulations! You beat the dealer!")
        elif playersScore == dealersScore:
            print("Honours even!")
        else:
            print("Too bad! The dealer has won.")

stillPlaying = True
while stillPlaying:
    main()
    choice = input("Play again? [Y/N]: ")
    if choice == "N":
        print("Goodbye!")
        stillPlaying = False
