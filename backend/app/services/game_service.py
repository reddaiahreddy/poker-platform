from app.poker.table import Table
from app.poker.player import Player


class GameService:
    def __init__(self):
        self.table = Table()

    def add_player(self, player_id: str, name: str):
        player = Player(id=player_id, name=name)
        self.table.add_player(player)

        return {
            "event": "player_joined",
            "player": name
        }

    def start_game(self):
        self.table.start_round()

        return {
            "event": "game_started",
            "players": [
                {
                    "name": p.name,
                    "hand": [str(c) for c in p.hand]
                }
                for p in self.table.players
            ]
        }

    def get_state(self):
        return {
            "players": [
                {
                    "name": p.name,
                    "chips": p.chips,
                    "folded": p.has_folded
                }
                for p in self.table.players
            ],
            "pot": self.table.pot,
            "state": self.table.state,
            "community_cards": [str(c) for c in self.table.community_cards]
        }