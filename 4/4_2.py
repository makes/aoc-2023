def count_matches(cardid):
    mynums = cards[cardid][0]
    winningnums = cards[cardid][1]
    matches = 0
    for num in mynums:
        if num in winningnums:
            matches += 1
    return matches


def count_cards(ids, winnings={}):
    n = 0
    for cardid in ids:
        if cardid not in winnings:
            m = count_matches(cardid)
            winnings[cardid] = list(range(cardid + 1, cardid + m + 1))
        n += 1 + count_cards(winnings[cardid], winnings)
    return n


if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    cards = {}

    for line in lines:
        idstr, numstr = line.split(":")
        mynums, winningnums = numstr.split("|")
        cardid = int(idstr.split()[1])
        cards[cardid] = [
            [int(x) for x in mynums.split()],
            [int(x) for x in winningnums.split()],
        ]

    print(count_cards(cards))
