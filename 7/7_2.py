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
    def __init__(self, symbols, bid):
        if not len(symbols) == 5:
            raise ValueError("Hand must contain five cards")
        self.bid = bid
        self._cards = [Card(s) for s in symbols]
        card_counts = Counter(list(symbols))
        n_jokers = card_counts.get('J', 0)
        del card_counts['J']
        strength = sorted(card_counts.values(), reverse=True) if card_counts else [0]
        strength[0] += n_jokers
        self._strength = tuple(strength)

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
