from app.poker.table import Table
from app.poker.player import Player
from app.poker.card import Card


table = Table()

player1 = Player(
    id="1",
    name="Reddy"
)

player2 = Player(
    id="2",
    name="John"
)

table.add_player(player1)
table.add_player(player2)

player1.hand = [
    Card("hearts", "A"),
    Card("spades", "A")
]

player2.hand = [
    Card("hearts", "K"),
    Card("spades", "Q")
]

table.community_cards = [
    Card("clubs", "7"),
    Card("diamonds", "10"),
    Card("hearts", "2")
]

table.pot = 500

result = table.determine_winner()

print(result)

print("Reddy chips:", player1.chips)
print("John chips:", player2.chips)
print("Remaining pot:", table.pot)