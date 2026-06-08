from typing import List, Optional
from app.poker.player import Player
from app.poker.deck import Deck
from app.poker.game_manager import GameManager

class Table:
    def __init__(self):
        # 🎮 Game state
        self.players: List[Player] = []
        self.deck = Deck()

        self.state = "WAITING"  # WAITING → PRE_FLOP → FLOP → TURN → RIVER → SHOWDOWN

        # 🧠 Betting system
        self.pot = 0
        self.current_bet = 0
        self.current_turn = 0

        # 🃏 Community cards
        self.community_cards = []

    # -----------------------------
    # PLAYER MANAGEMENT
    # -----------------------------
    def add_player(self, player: Player):
        self.players.append(player)

    def get_active_players(self):
        return [p for p in self.players if not p.has_folded]

    # -----------------------------
    # GAME START
    # -----------------------------
    def start_round(self):
        self.deck = Deck()
        self.deck.shuffle()

        self.pot = 0
        self.current_bet = 0
        self.current_turn = 0
        self.community_cards = []

        self.state = "PRE_FLOP"

        for player in self.players:
            player.reset_hand()
            player.add_card(self.deck.deal(1)[0])
            player.add_card(self.deck.deal(1)[0])

    # -----------------------------
    # TURN SYSTEM
    # -----------------------------
    def get_current_player(self) -> Optional[Player]:
        if not self.players:
            return None
        return self.players[self.current_turn]

    def next_turn(self):
        if not self.players:
            return None

        total = len(self.players)

        for _ in range(total):
            self.current_turn = (self.current_turn + 1) % total
            player = self.players[self.current_turn]

            if not player.has_folded:
                return player

    # -----------------------------
    # BETTING SYSTEM
    # -----------------------------
    def bet(self, player_id: str, amount: int):
        player = next(p for p in self.players if p.id == player_id)

        if player.has_folded:
            return {"error": "Player has folded"}

        player.chips -= amount
        player.current_bet += amount
        self.pot += amount

        player.has_acted = True
        self.current_bet = max(self.current_bet, amount)

        return {
            "event": "bet",
            "player": player.name,
            "amount": amount,
            "pot": self.pot
        }

    def call(self, player_id: str):
        player = next(p for p in self.players if p.id == player_id)

        if player.has_folded:
            return {"error": "Player has folded"}

        required = self.current_bet - player.current_bet

        player.chips -= required
        player.current_bet += required
        self.pot += required

        player.has_acted = True

        return {
            "event": "call",
            "player": player.name,
            "amount": required,
            "pot": self.pot
        }

    def fold(self, player_id: str):
        player = next(p for p in self.players if p.id == player_id)

        player.has_folded = True
        player.has_acted = True

        return {
            "event": "fold",
            "player": player.name
        }

    # -----------------------------
    # ROUND CONTROL
    # -----------------------------
    def reset_betting_round(self):
        for player in self.players:
            player.current_bet = 0
            player.has_acted = False

        self.current_bet = 0

    def is_round_complete(self):
        active = self.get_active_players()
        return len(active) > 0 and all(p.has_acted for p in active)

    def advance_if_ready(self):
        if self.is_round_complete():
            self.reset_betting_round()
            self.next_state()

    # -----------------------------
    # GAME STATE MACHINE
    # -----------------------------
    def next_state(self):
        if self.state == "PRE_FLOP":
            self.state = "FLOP"
            self.community_cards = self.deck.deal(3)

        elif self.state == "FLOP":
            self.state = "TURN"
            self.community_cards += self.deck.deal(1)

        elif self.state == "TURN":
            self.state = "RIVER"
            self.community_cards += self.deck.deal(1)

        elif self.state == "RIVER":
            self.state = "SHOWDOWN"

    # ----------------------------
    # DETERMINE WINNER
    # ----------------------------
    def determine_winner(self):

        winner = GameManager.determine_winner(
            self.players,
            self.community_cards
        )

        winning_player = winner["player"]

        winning_player.chips += self.pot

        result = {
            "winner": winning_player.name,
            "hand": winner["result"]["name"],
            "pot": self.pot
        }

        self.pot = 0

        return result    

    # -----------------------------
    # DEBUG / STATE EXPORT
    # -----------------------------
    def get_state(self):
        return {
            "state": self.state,
            "pot": self.pot,
            "current_bet": self.current_bet,
            "community_cards": [str(c) for c in self.community_cards],
            "players": [
                {
                    "name": p.name,
                    "chips": p.chips,
                    "folded": p.has_folded,
                    "current_bet": p.current_bet
                }
                for p in self.players
            ]
        }