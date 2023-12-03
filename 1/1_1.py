from string import digits

with open("input.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

sum = 0

for l in lines:
    d = ''.join(x for x in l if x in digits)
    sum += int(d[0] + d[-1])

print(sum)
