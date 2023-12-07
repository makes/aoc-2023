from math import floor, ceil


def n(time: int, dist: int):
    d = time * time - 4 * dist  # discriminant
    return ceil((time + d**0.5) / 2) - floor((time - d**0.5) / 2) - 1


if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    t, d = [int("".join(filter(lambda x: x.isdigit(), s))) for s in lines]
    print(n(t, d))
