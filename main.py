import random


class Card:
    def __init__(self, number, house):
        self.house = house
        self.number = number


HOUSE_NAME = ['Club', 'Spade', 'Diamond', 'Heart']


class Deck:

    def __init__(self):
        self.cards = []
        for house in HOUSE_NAME:
            for num in range(1, 14):
                new = Card(num, house)
                self.cards.append(new)

    def shuffle(self):
        random.shuffle(self.cards)

    def distribute(self, players):

        num = 52 / players
        if num % 1 == 0:
            num = int(num)
            hands = []
            for i in range(players):

                hands.append(self.cards[i * num:i * num + num])
            self.cards = []
            return hands
        else:
            return TypeError


if __name__ == "__main__":
    myDeck = Deck()
    myDeck.shuffle()
    hands = myDeck.distribute(4)
    for hand in hands:

        b = list(map(lambda x: (x.number, x.house), hand))
        print(b)
        print()
