from math import floor, ceil, prod


def n(time: int, dist: int):
    d = time * time - 4 * dist  # discriminant
    return ceil((time + d**0.5) / 2) - floor((time - d**0.5) / 2) - 1


if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
    vals = list(zip(lines[0].split()[1:], lines[1].split()[1:]))
    vals = [(int(x[0]), int(x[1])) for x in vals]

    print(prod(map(lambda x: n(x[0], x[1]), vals)))
