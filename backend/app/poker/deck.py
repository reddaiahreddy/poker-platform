import random
from app.poker.card import Card, SUITS, RANKS


class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in SUITS for rank in RANKS]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, num=1):
        dealt = self.cards[:num]
        self.cards = self.cards[num:]
        return dealt