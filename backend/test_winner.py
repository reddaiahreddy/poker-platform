from app.poker.card import Card
from app.poker.player import Player
from app.poker.game_manager import GameManager


player1 = Player(
    id="1",
    name="Reddy"
)

player2 = Player(
    id="2",
    name="John"
)


player1.hand = [
    Card("hearts", "A"),
    Card("spades", "A")
]

player2.hand = [
    Card("hearts", "K"),
    Card("spades", "Q")
]


community_cards = [
    Card("clubs", "7"),
    Card("diamonds", "10"),
    Card("hearts", "2")
]


winner = GameManager.determine_winner(
    [player1, player2],
    community_cards
)

print("Winner:", winner["player"].name)
print("Hand:", winner["result"]["name"])