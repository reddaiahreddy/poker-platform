from app.poker.card import Card
from app.poker.hand_evaluator import HandEvaluator


cards = [
    Card("hearts", "A"),
    Card("spades", "A"),
    Card("clubs", "A"),
    Card("diamonds", "K"),
    Card("hearts", "7"),
]

result = HandEvaluator.evaluate(cards)

print(result)