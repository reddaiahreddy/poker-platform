from app.poker.card import Card
from app.poker.hand_evaluator import HandEvaluator

cards = [
    Card("hearts", "2"),
    Card("hearts", "5"),
    Card("hearts", "8"),
    Card("hearts", "J"),
    Card("hearts", "K"),
]

print(HandEvaluator.evaluate(cards))