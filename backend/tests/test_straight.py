from app.poker.card import Card
from app.poker.hand_evaluator import HandEvaluator

cards = [
    Card("hearts", "5"),
    Card("clubs", "6"),
    Card("spades", "7"),
    Card("diamonds", "8"),
    Card("hearts", "9"),
]

print(HandEvaluator.evaluate(cards))