START = 'AAA'
GOAL = 'ZZZ'

if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as f:
        text = f.read()

    seq, net = text.split('\n\n')
    net = ''.join(filter(lambda x: x not in list('=(,)'), list(net))).strip()
    net = [x.split() for x in net.split('\n')]
    nodes = {x[0]: (x[1], x[2]) for x in net}

    node = START
    idx = 0
    steps = 0
    while node != GOAL:
        dir = 0 if seq[idx] == 'L' else 1
        node = nodes[node][dir]
        idx = idx + 1 if idx < len(seq) - 1 else 0
        steps += 1

    print(steps)
        
