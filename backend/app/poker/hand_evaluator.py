from collections import Counter


HAND_RANKS = {
    "HIGH_CARD": 1,
    "PAIR": 2,
    "TWO_PAIR": 3,
    "THREE_OF_A_KIND": 4,
}


class HandEvaluator:

    @staticmethod
    def evaluate(cards):
        """
        cards = list[Card]
        """

        ranks = [card.rank for card in cards]

        counter = Counter(ranks)

        counts = sorted(counter.values(), reverse=True)

        # Three of a Kind
        if counts[0] == 3:
            return {
                "rank": HAND_RANKS["THREE_OF_A_KIND"],
                "name": "THREE_OF_A_KIND"
            }

        # Two Pair
        if counts.count(2) >= 2:
            return {
                "rank": HAND_RANKS["TWO_PAIR"],
                "name": "TWO_PAIR"
            }

        # Pair
        if counts[0] == 2:
            return {
                "rank": HAND_RANKS["PAIR"],
                "name": "PAIR"
            }

        return {
            "rank": HAND_RANKS["HIGH_CARD"],
            "name": "HIGH_CARD"
        }