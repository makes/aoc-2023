from math import isqrt, prod


def is_square(x: int):
    return x == isqrt(x) ** 2


def n(time: int, dist: int):
    d = time * time - 4 * dist  # discriminant
    return int((time + d**0.5) / 2) - int((time - d**0.5) / 2) - is_square(d)


if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
    vals = list(zip(lines[0].split()[1:], lines[1].split()[1:]))
    vals = [(int(x[0]), int(x[1])) for x in vals]

    print(prod(map(lambda x: n(x[0], x[1]), vals)))
