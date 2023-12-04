with open("input.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

cards = {}

for line in lines:
    idstr, numstr = line.split(':')
    mynums, winningnums = numstr.split('|')
    cardid = int(idstr.split()[1])
    cards[cardid] = [[int(x) for x in mynums.split()],
                     [int(x) for x in winningnums.split()]]

matches = {}
for cardid, nums in cards.items():
    for num in nums[0]:
        if num in nums[1]:
            if cardid in matches:
                matches[cardid] += 1
            else:
                matches[cardid] = 1

points = 0
for n in matches.values():
    points += 2 ** (n-1)

print(points)

