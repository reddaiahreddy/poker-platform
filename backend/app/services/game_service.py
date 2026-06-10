from app.poker.table import Table
from app.poker.player import Player


class GameService:

    def __init__(self):
        self.table = Table()

    def add_player(self, player_id: str, name: str):

        existing = next(
            (p for p in self.table.players if p.id == player_id),
            None
        )

        if existing:
            return {
                "event": "player_exists",
                "player": name
            }

        player = Player(
            id=player_id,
            name=name
        )

        self.table.add_player(player)

        return {
            "event": "player_joined",
            "player": name
        }

    def start_game(self):

        self.table.start_round()

        return {
            "event": "game_started",
            "state": self.table.state,
            "players": [
                {
                    "name": p.name,
                    "hand": [str(card) for card in p.hand]
                }
                for p in self.table.players
            ]
        }

    def get_state(self):
        state = self.table.get_state()

        state["event"] = "table_state"

        return state

    def showdown(self):

        result = self.table.determine_winner()

        return {
            "event": "winner",
            **result
        }