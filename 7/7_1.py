from collections import Counter


class Card:
    symbols = "23456789TJQKA"

    def __init__(self, symbol):
        self._symbol = symbol
        self._ordinality = Card.symbols.index(symbol)

    def __str__(self):
        return self._symbol

    def __lt__(self, other):
        return self._ordinality < other._ordinality


class Hand:
    def __init__(self, symbols, bid):
        if not len(symbols) == 5:
            raise ValueError("Hand must contain five cards")
        self.bid = bid
        self._cards = [Card(s) for s in symbols]
        self._strength = tuple(sorted(Counter(list(symbols)).values(), reverse=True))

    def __lt__(self, other):
        if self._strength < other._strength:
            return True
        if self._strength == other._strength:
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
