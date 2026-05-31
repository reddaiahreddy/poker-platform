from dataclasses import dataclass, field
from typing import List
from app.poker.card import Card


@dataclass
class Player:
    id: str
    name: str
    chips: int = 1000
    hand: List[Card] = field(default_factory=list)

    # 🃏 BETTING STATE
    current_bet: int = 0
    has_folded: bool = False
    has_acted: bool = False

    def reset_hand(self):
        self.hand = []
        self.has_folded = False
        self.has_acted = False
        self.current_bet = 0

    def add_card(self, card: Card):
        self.hand.append(card)

    def fold(self):
        self.has_folded = True
        self.has_acted = True