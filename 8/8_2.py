from math import lcm

START = 'A'
GOAL = 'Z'

def count_steps(nodes, start):
    node = start
    idx = 0
    steps = 0
    while node[2] != GOAL:
        dir = 0 if seq[idx] == 'L' else 1
        node = nodes[node][dir]
        idx = idx + 1 if idx < len(seq) - 1 else 0
        steps += 1
    return steps

if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as f:
        text = f.read()
    # parse
    seq, net = text.split('\n\n')
    net = ''.join(filter(lambda x: x not in list('=(,)'), list(net))).strip()
    net = [x.split() for x in net.split('\n')]
    nodes = {x[0]: (x[1], x[2]) for x in net}
    # find steps for each path
    startnodes = [x for x in list(nodes.keys()) if x[2] == START]
    steps = [count_steps(nodes, x) for x in startnodes]
    # compute when their cycles meet
    print(lcm(*steps))
        
