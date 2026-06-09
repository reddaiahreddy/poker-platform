from collections import Counter


HAND_RANKS = {
    "HIGH_CARD": 1,
    "PAIR": 2,
    "TWO_PAIR": 3,
    "THREE_OF_A_KIND": 4,
    "STRAIGHT": 5,
    "FLUSH": 6,
    "FULL_HOUSE": 7,
    "FOUR_OF_A_KIND": 8,
    "STRAIGHT_FLUSH": 9,
    "ROYAL_FLUSH": 10
}


RANK_VALUES = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14
}


class HandEvaluator:

    @staticmethod
    def is_flush(cards):
        suits = [card.suit for card in cards]
        counts = Counter(suits)

        return max(counts.values()) >= 5

    @staticmethod
    def is_straight(cards):

        values = sorted(
            set(RANK_VALUES[card.rank] for card in cards)
        )

        # Handle A-2-3-4-5 straight
        if 14 in values:
            values.insert(0, 1)

        consecutive = 1

        for i in range(1, len(values)):
            if values[i] == values[i - 1] + 1:
                consecutive += 1

                if consecutive >= 5:
                    return True
            else:
                consecutive = 1

        return False

    @staticmethod
    def evaluate(cards):

        ranks = [card.rank for card in cards]

        counter = Counter(ranks)

        counts = sorted(counter.values(), reverse=True)

        is_flush = HandEvaluator.is_flush(cards)
        is_straight = HandEvaluator.is_straight(cards)

        # Royal Flush
        if is_flush:
            values = sorted(
                set(RANK_VALUES[c.rank] for c in cards)
            )

            if {10, 11, 12, 13, 14}.issubset(values):
                return {
                    "rank": HAND_RANKS["ROYAL_FLUSH"],
                    "name": "ROYAL_FLUSH"
                }

        # Straight Flush
        if is_flush and is_straight:
            return {
                "rank": HAND_RANKS["STRAIGHT_FLUSH"],
                "name": "STRAIGHT_FLUSH"
            }

        # Four of a Kind
        if counts[0] == 4:
            return {
                "rank": HAND_RANKS["FOUR_OF_A_KIND"],
                "name": "FOUR_OF_A_KIND"
            }

        # Full House
        if len(counts) >= 2 and counts[0] == 3 and counts[1] >= 2:
            return {
                "rank": HAND_RANKS["FULL_HOUSE"],
                "name": "FULL_HOUSE"
            }

        # Flush
        if is_flush:
            return {
                "rank": HAND_RANKS["FLUSH"],
                "name": "FLUSH"
            }

        # Straight
        if is_straight:
            return {
                "rank": HAND_RANKS["STRAIGHT"],
                "name": "STRAIGHT"
            }

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