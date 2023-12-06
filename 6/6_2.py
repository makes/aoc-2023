from math import isqrt


def is_square(x: int):
    return x == isqrt(x) ** 2


def n(time: int, dist: int):
    d = time * time - 4 * dist  # discriminant
    return int((time + d**0.5) / 2) - int((time - d**0.5) / 2) - is_square(d)


if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    t, d = [int("".join(filter(lambda x: x.isdigit(), s))) for s in lines]
    print(n(t, d))
