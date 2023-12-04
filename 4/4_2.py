with open("input.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

card_info = {}

for line in lines:
    idstr, numstr = line.split(':')
    mynums, winningnums = numstr.split('|')
    cardid = int(idstr.split()[1])
    card_info[cardid] = [[int(x) for x in mynums.split()],
                         [int(x) for x in winningnums.split()]]

def count_matches(cardid):
    mynums = card_info[cardid][0]
    winningnums = card_info[cardid][1]
    matches = 0
    for num in mynums:
        if num in winningnums:
            matches += 1
    return matches

cards = {}
def count_cards(ids):
    n = 0
    for cardid in ids:
        matches = count_matches(cardid)
        n += 1
        if matches > 0:
            n += count_cards(list(range(cardid + 1, cardid + matches + 1)))
    return n

print(count_cards(card_info))

