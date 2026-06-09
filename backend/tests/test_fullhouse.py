from app.poker.card import Card
from app.poker.hand_evaluator import HandEvaluator

cards = [
    Card("hearts", "A"),
    Card("clubs", "A"),
    Card("spades", "A"),
    Card("diamonds", "K"),
    Card("hearts", "K"),
]

print(HandEvaluator.evaluate(cards))