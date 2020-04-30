import random

HOUSE_NAME = ['Club', 'Spade', 'Diamond', 'Heart']


class Card:
    def __init__(self, number, house):
        self.house = house
        self.number = number


class Hand:
    def __init__(self, size):
        self.size = size
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def drop(self, card):
        if card in self.cards:
            self.cards.remove(card)

    def arrange(self, key):
        return NotImplementedError

    def __iter__(self):
        for card in self.cards:
            yield card


class Deck:

    def __init__(self):
        self.cards = []
        for house in HOUSE_NAME:
            for num in range(1, 14):
                new = Card(num, house)
                self.cards.append(new)

    def shuffle(self):
        random.shuffle(self.cards)

    def getCard(self):
        return self.cards.pop()

    def distribute(self, playersNum, count=None):

        num = 52 / playersNum
        if (count == None and num % 1 == 0) or num >= count:

            count = int(num) if count == None else count

            players = [Hand(count) for i in range(playersNum)]

            round = 1
            while round <= count:
                for player in players:
                    player.add(self.getCard())

                round += 1
            return players

        else:
            return TypeError


if __name__ == "__main__":
    myDeck = Deck()
    myDeck.shuffle()

    # print(myDeck.getCard().number)
    # print(len(myDeck.cards))
    hands = myDeck.distribute(4, 3)
    for hand in hands:
        b = list(map(lambda x: (x.number, x.house), hand))
        print(b)
        print()
