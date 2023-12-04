with open("input.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

cards = {}

for line in lines:
    idstr, numstr = line.split(':')
    mynums, winningnums = numstr.split('|')
    cardid = int(idstr.split()[1])
    cards[cardid] = [[int(x) for x in mynums.split()],
                         [int(x) for x in winningnums.split()]]

def count_matches(cardid):
    mynums = cards[cardid][0]
    winningnums = cards[cardid][1]
    matches = 0
    for num in mynums:
        if num in winningnums:
            matches += 1
    return matches

matches = {cid: count_matches(cid) for cid in cards}

def count_cards(ids):
    n = 0
    for cardid in ids:
        m = matches[cardid]
        n += 1
        if m > 0:
            n += count_cards(list(range(cardid + 1, cardid + m + 1)))
    return n

print(count_cards(cards))

