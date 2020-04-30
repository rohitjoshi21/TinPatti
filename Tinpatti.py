import card

playerNo = int(input('Enter no of player? '))

myDeck = card.Deck()
myDeck.shuffle()
hands = myDeck.distribute(playerNo, 3)
for hand in hands:

    b = list(map(lambda x: (x.number, x.house), hand))
    print(b)
    print()
