from collections import Counter


class Card:
    symbols = "J23456789TQKA"

    def __init__(self, symbol):
        self._symbol = symbol
        self._ordinality = Card.symbols.index(symbol)

    def __str__(self):
        return self._symbol

    def __lt__(self, other):
        return self._ordinality < other._ordinality


class Hand:
    types = {
        (1, 1, 1, 1, 1): 0,  # High card
        (1, 1, 1, 2): 1,  # One pair
        (1, 2, 2): 2,  # Two pair
        (1, 1, 3): 3,  # Three of a kind
        (2, 3): 4,  # Full house
        (1, 4): 5,  # Four of a kind
        (5,): 6,  # Five of a kind
    }

    def __init__(self, symbols, bid):
        if not len(symbols) == 5:
            raise ValueError("Hand must contain five cards")
        self.bid = bid
        self._cards = [Card(s) for s in symbols]
        card_counts = Counter(list(symbols))
        n_jokers = 0 if "J" not in card_counts else card_counts["J"]
        no_jokers = dict(filter(lambda x: x[0] != "J", card_counts.items()))
        type_id = sorted(no_jokers.values()) if no_jokers else [0]
        type_id[-1] += n_jokers
        self._type_id = tuple(type_id)
        self._value = Hand.types[self._type_id]

    def __lt__(self, other):
        if self._value < other._value:
            return True
        if self._value == other._value:
            for c in zip(self._cards, other._cards):
                if c[0] < c[1]:
                    return True
                if c[1] < c[0]:
                    break
        return False


if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    hands = sorted([Hand(s.split()[0], int(s.split()[1])) for s in lines])
    print(sum((i + 1) * h.bid for i, h in enumerate(hands)))
