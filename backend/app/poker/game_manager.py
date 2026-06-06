from app.poker.hand_evaluator import HandEvaluator


class GameManager:

    @staticmethod
    def determine_winner(players, community_cards):

        ranked_players = []

        for player in players:

            if player.has_folded:
                continue

            all_cards = player.hand + community_cards

            result = HandEvaluator.evaluate(all_cards)

            ranked_players.append({
                "player": player,
                "result": result
            })

        ranked_players.sort(
            key=lambda x: x["result"]["rank"],
            reverse=True
        )

        return ranked_players[0]